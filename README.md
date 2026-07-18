# Enkripsi Gambar Berbasis Chaotic Logistic Map dan Linear Feedback Shift Register

Repositori ini berisi implementasi algoritma enkripsi dan dekripsi citra digital sebagai bagian dari Tugas Akhir. Sistem ini dirancang untuk mengamankan citra (gambar) menggunakan pendekatan *Chaos Theory* dan pembangkit bilangan acak semu (PRNG).

## Fitur Utama
*   **Kunci Dinamis (Plaintext-Dependent):** Nilai awal (seed) modifikasi *Logistic Map* sangat sensitif terhadap perubahan citra asli (bahkan pada 1 piksel) berdasarkan total nilai piksel citra.
*   **Chaotic Logistic Map:** Digunakan untuk menghasilkan deret *chaos* dalam proses *Confusion* (pengacakan posisi piksel).
*   **Linear Feedback Shift Register (LFSR):** Digunakan untuk menghasilkan *key stream* pseudo-acak.
*   **Proses Difusi Ganda:** Menggunakan metode *Forward Diffusion* dan *Backward Diffusion* untuk menyebarkan pengaruh piksel secara merata.

## Struktur Direktori

Berdasarkan struktur proyek, berikut adalah fungsi dari masing-masing komponen:

*   **`data/`**: Direktori untuk menyimpan citra.
    *   `plaintext/`: Tempat menaruh citra asli yang akan dienkripsi.
    *   `ciphertext/`: Tempat penyimpanan otomatis untuk hasil enkripsi citra.
    *   `decrypted/`: Tempat penyimpanan otomatis untuk hasil dekripsi citra.
*   **`encryption.py`**: Skrip utama untuk menjalankan proses enkripsi dari folder `plaintext` ke `ciphertext`.
*   **`decryption.py`**: Skrip utama untuk mengembalikan citra dari folder `ciphertext` ke `decrypted`.
*   **`logistic_map.py`**: Modul fungsi *Chaotic Logistic Map* pembentuk sekuens acak.
*   **`lfsr.py`**: Modul fungsi *Linear Feedback Shift Register* pembentuk aliran bit.
*   **`catatan_kunci.txt`**: File penyimpanan otomatis yang berisi *dictionary* Python (`DARI_DATA_PENGUJIAN`) untuk mencatat total nilai piksel setiap gambar guna rekonstruksi kunci saat dekripsi.

## Prasyarat (Requirements)

Untuk menjalankan kode ini, pastikan Anda telah menginstal pustaka Python berikut:
*   `numpy` (Untuk komputasi array dan matriks)
*   `opencv-python` / `cv2` (Untuk pembacaan dan penulisan citra *grayscale*)
*   `os` (Pustaka bawaan Python untuk manajemen path file)

Anda dapat menginstalnya menggunakan pip:
```bash
pip install numpy opencv-python
```

## Cara Penggunaan

### 1. Proses Enkripsi
1.  Buat folder `data/plaintext/` di dalam direktori kerja Anda (jika belum ada).
2.  Masukkan citra digital Anda (format `.tif`, `.png`, atau `.jpg`) ke dalam folder `data/plaintext/`.
3.  Jalankan skrip enkripsi:
    ```bash
    python encryption.py
    ```
4.  Hasil enkripsi akan tersimpan otomatis di `data/ciphertext/` dan program akan menggenerate file `catatan_kunci.txt`.

### 2. Proses Dekripsi
1.  Pastikan citra terenkripsi ada di folder `data/ciphertext/` dan file `catatan_kunci.txt` tersedia di folder yang sama dengan skrip.
2.  Jalankan skrip dekripsi:
    ```bash
    python decryption.py
    ```
3.  Citra hasil pemulihan (dekripsi) akan tersimpan secara otomatis di dalam folder `data/decrypted/` dengan awalan nama `decrypted_`.

## Catatan Tambahan
*   Program ini membaca citra dalam mode *Grayscale* (skala abu-abu) secara otomatis menggunakan `cv2.IMREAD_GRAYSCALE`.
*   File `catatan_kunci.txt` bersifat rahasia dan wajib disertakan saat melakukan dekripsi agar kunci dinamis dapat direkonstruksi secara presisi. Jika file ini hilang, program akan mencoba menggunakan *fallback parameter* berdasarkan jumlah nilai citra cipher, yang mungkin tidak akurat.

## Lisensi

Proyek ini dilisensikan di bawah **MIT License**. Anda bebas menggunakan, memodifikasi, dan mendistribusikan kode ini sesuai dengan ketentuan lisensi.

Lihat file [LICENSE](LICENSE) untuk detail lengkap.
