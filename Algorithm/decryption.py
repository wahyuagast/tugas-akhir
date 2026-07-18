import os
import cv2
import numpy as np

# =========================================================================
# 1. KOMPONEN ALGORITMA DEKRIPSI (INVERS MATEMATIS)
# =========================================================================

def lfsr(seed, taps, length):
    """Membangkitkan ulang pseudo-random bit LFSR yang sama dengan enkripsi"""
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
    """Membangkitkan ulang chaotic sequence dengan seed x0 yang dinamis"""
    x = np.zeros(size)
    x[0] = x0
    for i in range(1, size):
        x[i] = r * x[i-1] * (1 - x[i-1])
    return x

def decrypt_image(img_cipher, plaintext_factor):
    """
    Fungsi utama untuk mendekripsi citra (Ciphertext -> Plaintext)
    """
    rows, cols = img_cipher.shape
    size = rows * cols
    backward_enc = [int(p) for p in img_cipher.flatten()]

    # Rekonstruksi Kunci Dinamis berdasarkan parameter plaintext_factor
    x0_modified = (0.123456789 + plaintext_factor) % 1.0
    if x0_modified == 0.0:
        x0_modified = 0.5

    # Bangkitkan kembali deret chaos dan matriks indeks pengacakan
    chaos = logistic_map(x0_modified, 3.99, size)
    indices = np.argsort(chaos)

    # Bangkitkan kembali keystream LFSR
    key_stream = lfsr(0b10101010, [7, 5, 4, 3], size)
    key_stream = [int(k * 255) for k in key_stream]

    # Langkah I: Reverse Backward Diffusion
    forward_enc = [0] * size
    prev = 0
    for i in reversed(range(size)):
        forward_enc[i] = (backward_enc[i] - prev) % 256
        prev = backward_enc[i]

    # Langkah II: Reverse Forward Diffusion
    shuffled = [0] * size
    prev = 0
    for i in range(size):
        chaos_val = int(chaos[i] * 255)
        shuffled[i] = (forward_enc[i] - key_stream[i] - chaos_val - prev) % 256
        prev = forward_enc[i]

    # Langkah III: De-shuffling (Mengembalikan urutan posisi piksel semula)
    flat_decrypted = [0] * size
    for i in range(size):
        flat_decrypted[indices[i]] = shuffled[i]

    return np.array(flat_decrypted, dtype=np.uint8).reshape(rows, cols)


# =========================================================================
# 2. RUNTIME EKSEKUSI OTOMATIS DENGAN PEMBACAAN FILE KUNCI
# =========================================================================

FOLDER_CIPHER = "data/ciphertext"
FOLDER_DEKRIPSI = "data/decrypted"
FILE_CATATAN = "catatan_kunci.txt"

if __name__ == "__main__":
    if not os.path.exists(FOLDER_DEKRIPSI):
        os.makedirs(FOLDER_DEKRIPSI)

    if not os.path.exists(FOLDER_CIPHER):
        print(f"Error: Folder '{FOLDER_CIPHER}' tidak ditemukan.")
        exit()

    # Membaca file catatan_kunci.txt secara dinamis menggunakan fungsi exec() Python
    dari_data_pengujian = {}
    if os.path.exists(FILE_CATATAN):
        try:
            with open(FILE_CATATAN, "r") as f:
                konten = f.read()
                # Eksekusi string python ke dalam local scope dictionary
                lokal = {}
                exec(konten, {}, lokal)
                if "DARI_DATA_PENGUJIAN" in lokal:
                    dari_data_pengujian = lokal["DARI_DATA_PENGUJIAN"]
            print(f"[INFO] Berhasil memuat file kunci otomatis '{FILE_CATATAN}'")
        except Exception as e:
            print(f"[PERINGATAN] Gagal membaca file kunci karena: {e}. Menggunakan fallback.")
    else:
        print(f"[PERINGATAN] File '{FILE_CATATAN}' tidak ditemukan. Menggunakan fallback.")

    print("\nPROSES DEKRIPSI CITRA SEDANG BERJALAN...")
    print("=" * 70)

    berhasil = 0
    for filename in os.listdir(FOLDER_CIPHER):
        if not filename.lower().endswith((".tif", ".tiff", ".png", ".jpg", ".jpeg")):
            continue

        path_cipher = os.path.join(FOLDER_CIPHER, filename)
        img_cipher = cv2.imread(path_cipher, cv2.IMREAD_GRAYSCALE)

        if img_cipher is None:
            continue

        rows, cols = img_cipher.shape

        # Mengambil nilai parameter kunci dinamis dari file catatan
        if filename in dari_data_pengujian:
            total_sum_asli = dari_data_pengujian[filename]
            plaintext_factor = total_sum_asli / (255.0 * rows * cols)
        else:
            # Fallback jika nama file tidak terdata di berkas catatan_kunci.txt
            plaintext_factor = np.sum(img_cipher) / (255.0 * rows * cols)

        # Eksekusi fungsi dekripsi
        img_plain = decrypt_image(img_cipher, plaintext_factor)

        # Simpan hasil pemulihan citra ke folder tujuan
        path_output = os.path.join(FOLDER_DEKRIPSI, f"decrypted_{filename}")
        cv2.imwrite(path_output, img_plain)
        
        print(f"[SUKSES] Dekripsi: {filename} -> 'decrypted_{filename}'")
        berhasil += 1

    print("=" * 70)
    print(f"Selesai! Total {berhasil} citra berhasil didekripsi ke folder '{FOLDER_DEKRIPSI}'.")