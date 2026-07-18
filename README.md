# Enkripsi Gambar Berbasis *Chaotic Logistic Map* dan *Linear Feedback Shift Register*

Repositori ini berisi implementasi algoritma enkripsi dan dekripsi citra digital sebagai bagian dari Tugas Akhir. Sistem dirancang untuk mengamankan citra (*image encryption*) menggunakan kombinasi *Chaos Theory* melalui *Chaotic Logistic Map* dan pembangkit bilangan acak semu (*Pseudo-Random Number Generator* / PRNG) berbasis *Linear Feedback Shift Register* (LFSR).

## Fitur Utama

* **Kunci Dinamis (*Plaintext-Dependent*)**
  Nilai awal (*seed*) pada *Logistic Map* dimodifikasi berdasarkan total nilai piksel citra asli. Dengan demikian, perubahan sekecil apa pun pada citra (bahkan satu piksel) akan menghasilkan parameter kunci yang berbeda.

* **Chaotic Logistic Map**
  Digunakan untuk menghasilkan deret *chaos* yang berperan dalam proses *confusion* (pengacakan posisi piksel).

* **Linear Feedback Shift Register (LFSR)**
  Digunakan untuk menghasilkan *key stream* pseudo-acak yang digunakan dalam proses difusi.

* **Proses Difusi Ganda**
  Menggunakan kombinasi *Forward Diffusion* dan *Backward Diffusion* untuk menyebarkan perubahan nilai piksel secara merata ke seluruh citra.

* **Dekripsi Deterministik**
  Citra terenkripsi dapat dipulihkan kembali secara utuh apabila parameter kunci dinamis berhasil direkonstruksi.

---

## Struktur Direktori

```text
.
├── data/
│   ├── plaintext/
│   ├── ciphertext/
│   └── decrypted/
├── encryption.py
├── decryption.py
├── logistic_map.py
├── lfsr.py
├── catatan_kunci.txt
├── requirements.txt
└── README.md
```

### Keterangan

* **`data/plaintext/`**
  Menyimpan citra asli yang akan dienkripsi.

* **`data/ciphertext/`**
  Menyimpan hasil enkripsi citra.

* **`data/decrypted/`**
  Menyimpan hasil dekripsi citra.

* **`encryption.py`**
  Skrip utama untuk proses enkripsi.

* **`decryption.py`**
  Skrip utama untuk proses dekripsi.

* **`logistic_map.py`**
  Implementasi fungsi *Chaotic Logistic Map*.

* **`lfsr.py`**
  Implementasi fungsi *Linear Feedback Shift Register*.

* **`catatan_kunci.txt`**
  Berkas yang dibuat otomatis untuk menyimpan informasi yang diperlukan dalam rekonstruksi parameter kunci saat proses dekripsi.

---

## Prasyarat

Pastikan lingkungan pengembangan telah memenuhi kebutuhan berikut:

* Python 3.8 atau lebih baru
* NumPy
* OpenCV-Python

### Instalasi Dependensi

Menggunakan pip:

```bash
pip install numpy opencv-python
```

Atau menggunakan file `requirements.txt`:

```bash
pip install -r requirements.txt
```

Contoh isi `requirements.txt`:

```text
numpy
opencv-python
```

---

## Cara Penggunaan

### 1. Proses Enkripsi

1. Buat folder:

```text
data/plaintext/
```

2. Masukkan citra yang akan dienkripsi ke dalam folder tersebut.

   Format yang didukung:

   * `.tif`
   * `.tiff`
   * `.png`
   * `.jpg`
   * `.jpeg`

3. Jalankan proses enkripsi:

```bash
python encryption.py
```

4. Hasil akan tersimpan pada:

```text
data/ciphertext/
```

5. Program akan membuat file:

```text
catatan_kunci.txt
```

yang diperlukan untuk proses dekripsi.

---

### 2. Proses Dekripsi

1. Pastikan citra terenkripsi tersedia di folder:

```text
data/ciphertext/
```

2. Pastikan file:

```text
catatan_kunci.txt
```

berada pada direktori yang sama dengan skrip.

3. Jalankan proses dekripsi:

```bash
python decryption.py
```

4. Hasil pemulihan citra akan disimpan pada:

```text
data/decrypted/
```

dengan format nama:

```text
decrypted_nama_file.ext
```

---

## Alur Algoritma

### Enkripsi

1. Membaca citra *grayscale*.
2. Menghitung nilai *plaintext-dependent factor*.
3. Memodifikasi *seed* *Logistic Map*.
4. Menghasilkan deret *chaos*.
5. Melakukan *confusion* (pengacakan posisi piksel).
6. Menghasilkan *key stream* menggunakan LFSR.
7. Melakukan *Forward Diffusion*.
8. Melakukan *Backward Diffusion*.
9. Menyimpan citra terenkripsi.

### Dekripsi

1. Membaca citra terenkripsi.
2. Meregenerasi parameter *chaos*.
3. Meregenerasi *key stream* LFSR.
4. Melakukan invers *Backward Diffusion*.
5. Melakukan invers *Forward Diffusion*.
6. Melakukan *de-shuffling*.
7. Mengembalikan citra asli.

---

## Catatan Penting

* Program membaca citra menggunakan mode *grayscale* (`cv2.IMREAD_GRAYSCALE`).
* File `catatan_kunci.txt` diperlukan untuk merekonstruksi parameter kunci secara akurat saat dekripsi.
* Jika file tersebut tidak tersedia, program akan menggunakan mekanisme *fallback* yang mungkin menghasilkan hasil dekripsi yang tidak sesuai dengan citra asli.

### Keamanan

⚠️ File `catatan_kunci.txt` mengandung informasi yang digunakan dalam rekonstruksi kunci dinamis. Untuk penggunaan pada data sensitif, hindari membagikan file ini kepada pihak yang tidak berwenang.

⚠️ Implementasi ini dikembangkan untuk tujuan penelitian dan akademik. Sebelum digunakan pada sistem produksi atau aplikasi keamanan nyata, diperlukan evaluasi kriptanalisis yang lebih mendalam.

---

## Lisensi

Proyek ini dilisensikan di bawah **MIT License**.

Anda bebas menggunakan, memodifikasi, mendistribusikan, dan mengembangkan proyek ini sesuai ketentuan yang tercantum dalam file `LICENSE`.

Lihat file `LICENSE` untuk informasi lengkap.
