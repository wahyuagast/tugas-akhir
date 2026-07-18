import os
import cv2
import numpy as np

# =========================================================================
# 1. KOMPONEN ALGORITMA ENKRIPSI
# =========================================================================

def lfsr(seed, taps, length):
    """
    Fungsi Linear Feedback Shift Register (LFSR) untuk menghasilkan pseudo-random bit.
    """
    sr = seed
    output = []
    for _ in range(length):
        bit = 0
        for t in taps:
            bit ^= (sr >> t) & 1

        sr = (sr >> 1) | (bit << 7)
        output.append(sr & 1)

    return output


def logistic_map(x0, r, size):
    """
    Fungsi Chaotic Logistic Map.
    """
    x = np.zeros(size)
    x[0] = x0

    for i in range(1, size):
        x[i] = r * x[i-1] * (1 - x[i-1])

    return x


def encrypt_image(img):
    """
    Fungsi utama untuk mengenkripsi citra.
    """
    rows, cols = img.shape

    # 1. Meratakan gambar (Flattening)
    flat = []
    for i in range(rows):
        for j in range(cols):
            flat.append(int(img[i][j]))

    size = len(flat)

    # ==========================================
    # Plaintext-dependent Keystream
    # ==========================================
    # Menghitung faktor dari citra asli (berubah jika 1 piksel saja diubah)
    plaintext_factor = np.sum(img) / (255.0 * rows * cols)
    
    # Memodifikasi nilai awal (seed) x0 menggunakan faktor plaintext
    x0_modified = (0.123456789 + plaintext_factor) % 1.0
    
    if x0_modified == 0.0:
        x0_modified = 0.5
    # ==========================================

    # 2. Generate Chaos Sequence dengan x0 yang sudah sensitif terhadap citra
    chaos = logistic_map(x0_modified, 3.99, size)

    # 3. Proses Confusion (Pengacakan/Shuffling)
    indices = np.argsort(chaos)
    shuffled = []
    for idx in indices:
        shuffled.append(flat[int(idx)])

    # 4. Generate Key Stream menggunakan LFSR
    key_stream = lfsr(0b10101010, [7, 5, 4, 3], size)
    key_stream = [int(k * 255) for k in key_stream]

    # 5. Proses Forward Diffusion
    encrypted = []
    prev = 0
    for i in range(size):
        chaos_val = int(chaos[i] * 255)
        val = (shuffled[i] + key_stream[i] + chaos_val + prev) % 256
        encrypted.append(val)
        prev = val

    # 6. Proses Backward Diffusion
    backward_enc = list(encrypted)
    prev = 0
    for i in reversed(range(size)):
        backward_enc[i] = (encrypted[i] + prev) % 256
        prev = backward_enc[i]

    # 7. Membentuk kembali array menjadi matriks citra 2D
    encrypted_img = np.array(backward_enc, dtype=np.uint8).reshape(rows, cols)

    return encrypted_img, np.sum(img)


# =========================================================================
# 2. RUNTIME EKSEKUSI OTOMATIS ATAS FOLDER PLAINTEXT
# =========================================================================

FOLDER_PLAINTEXT = "data/plaintext"
FOLDER_CIPHERTEXT = "data/ciphertext"
FILE_CATATAN = "catatan_kunci.txt"

if __name__ == "__main__":
    if not os.path.exists(FOLDER_CIPHERTEXT):
        os.makedirs(FOLDER_CIPHERTEXT)

    if not os.path.exists(FOLDER_PLAINTEXT):
        print(f"Error: Folder '{FOLDER_PLAINTEXT}' tidak ditemukan. Silakan buat folder dan masukkan gambar asli Anda.")
        exit()

    print("PROSES ENKRIPSI CITRA SEDANG BERJALAN...")
    print("=" * 70)

    berhasil = 0
    
    # Buka file teks untuk menyimpan nilai secara otomatis
    with open(FILE_CATATAN, "w") as f_catat:
        f_catat.write("DARI_DATA_PENGUJIAN = {\n")
        
        for filename in os.listdir(FOLDER_PLAINTEXT):
            if not filename.lower().endswith((".tif", ".tiff", ".png", ".jpg", ".jpeg")):
                continue

            path_plain = os.path.join(FOLDER_PLAINTEXT, filename)
            img_original = cv2.imread(path_plain, cv2.IMREAD_GRAYSCALE)

            if img_original is None:
                continue

            # Eksekusi fungsi enkripsi
            img_cipher, total_piksel_asli = encrypt_image(img_original)

            # Simpan hasil enkripsi ke folder tujuan
            path_output = os.path.join(FOLDER_CIPHERTEXT, filename)
            cv2.imwrite(path_output, img_cipher)
            
            # Tulis ke file txt dengan format dictionary Python langsung
            f_catat.write(f"    \"{filename}\": {total_piksel_asli},\n")
            
            print(f"[SUKSES] Enkripsi: {filename}")
            berhasil += 1
            
        f_catat.write("}\n")

    print("=" * 70)
    print(f"Selesai! Total {berhasil} citra dienkripsi.")
    print(f"Catatan kunci otomatis disimpan ke file: '{FILE_CATATAN}'")