# Image Encryption Using *Chaotic Logistic Map* and *Linear Feedback Shift Register* (LFSR)

🇮🇩 Versi Bahasa Indonesia tersedia di bawah halaman ini.

---

## English

### Overview

This repository contains an implementation of an image encryption and decryption algorithm developed as part of an undergraduate thesis project. The system secures digital images (*image encryption*) using a combination of *Chaos Theory* through a *Chaotic Logistic Map* and a *Pseudo-Random Number Generator* (PRNG) based on a *Linear Feedback Shift Register* (LFSR).

### Key Features

* **Dynamic Key (*Plaintext-Dependent*)**

  * The initial *seed* of the *Logistic Map* is modified according to the total pixel intensity of the original image. Even a one-pixel change produces a different key parameter.

* **Chaotic Logistic Map**

  * Generates a chaotic sequence used in the *confusion* stage (*pixel shuffling*).

* **Linear Feedback Shift Register (LFSR)**

  * Generates a pseudo-random *key stream* used during diffusion.

* **Double Diffusion Process**

  * Combines *Forward Diffusion* and *Backward Diffusion* to distribute pixel influence across the entire image.

* **Deterministic Decryption**

  * The encrypted image can be reconstructed exactly when the dynamic key parameters are available.

### Directory Structure

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

### Requirements

* Python 3.8+
* NumPy
* OpenCV-Python

Installation:

```bash
pip install -r requirements.txt
```

### Usage

#### Encryption

```bash
python encryption.py
```

Input images should be placed in:

```text
data/plaintext/
```

Encrypted images will be generated in:

```text
data/ciphertext/
```

#### Decryption

```bash
python decryption.py
```

Decrypted images will be generated in:

```text
data/decrypted/
```

### Notes

* Images are automatically processed in *grayscale* mode.
* The file `catatan_kunci.txt` is required to reconstruct dynamic key parameters during decryption.
* Missing key records may result in inaccurate reconstruction.

### Security Notice

⚠️ This implementation was developed for academic and research purposes. Additional cryptanalysis and security evaluation are recommended before production use.

---

# Enkripsi Gambar Berbasis *Chaotic Logistic Map* dan *Linear Feedback Shift Register* (LFSR)

## Bahasa Indonesia

### Deskripsi

Repositori ini berisi implementasi algoritma enkripsi dan dekripsi citra digital sebagai bagian dari Tugas Akhir. Sistem dirancang untuk mengamankan citra (*image encryption*) menggunakan kombinasi *Chaos Theory* melalui *Chaotic Logistic Map* dan pembangkit bilangan acak semu (*Pseudo-Random Number Generator* / PRNG) berbasis *Linear Feedback Shift Register* (LFSR).

### Fitur Utama

* **Kunci Dinamis (*Plaintext-Dependent*)**

  * Nilai awal (*seed*) dimodifikasi berdasarkan total nilai piksel citra asli.

* **Chaotic Logistic Map**

  * Digunakan untuk menghasilkan deret *chaos* pada proses *confusion*.

* **Linear Feedback Shift Register (LFSR)**

  * Digunakan untuk menghasilkan *key stream* pseudo-acak.

* **Proses Difusi Ganda**

  * Menggunakan *Forward Diffusion* dan *Backward Diffusion*.

* **Dekripsi Deterministik**

  * Citra dapat dipulihkan kembali secara utuh jika parameter kunci tersedia.

### Struktur Direktori

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

### Prasyarat

* Python 3.8+
* NumPy
* OpenCV-Python

Instalasi:

```bash
pip install -r requirements.txt
```

### Cara Penggunaan

#### Enkripsi

```bash
python encryption.py
```

Masukkan citra ke:

```text
data/plaintext/
```

Hasil enkripsi akan tersimpan di:

```text
data/ciphertext/
```

#### Dekripsi

```bash
python decryption.py
```

Hasil dekripsi akan tersimpan di:

```text
data/decrypted/
```

### Catatan

* Program membaca citra dalam mode *grayscale*.
* File `catatan_kunci.txt` diperlukan untuk merekonstruksi parameter kunci saat dekripsi.
* Jika file tersebut hilang, hasil dekripsi mungkin tidak identik dengan citra asli.

### Keamanan

⚠️ Implementasi ini dikembangkan untuk tujuan penelitian dan akademik. Sebelum digunakan pada sistem produksi, diperlukan evaluasi keamanan yang lebih mendalam.

---

## License

This project is licensed under the **MIT License**.

See the `LICENSE` file for details.
