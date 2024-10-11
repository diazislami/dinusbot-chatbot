# Chatbot Layanan Akademik

Repositori ini berisi sebuah proyek tugas akhir (skripsi) yang berupa chatbot layanan akademik dengan menerapkan algoritma LSTM. Penerapan algoritma LSTM dibantu dengan penggunaan Tensorflow yang diintegrasikan pada web dengan menggunakan Flask. Tampilan web dibuat sedikit mirip dengan tampilan web kampus dengan tujuan untuk memberikan pengalaman nyata pada pengguna terkait layanan akademik melalui chatbot. Layanan akademik yang dimaksud ialah layanan berupa tanya jawab terkait informasi seputar akademik kampus kepada pengguna.

## Daftar Isi
- [Instalasi](#instalasi)
  - [1. Membuat Virtual Environment](#1-membuat-virtual-environment)
  - [2. Menginstal Library yang Dibutuhkan](#2-menginstal-library-yang-dibutuhkan)
  - [3. Menjalankan Aplikasi](#3-menjalankan-aplikasi)

## Instalasi

Untuk menjalankan proyek ini secara lokal, ikuti langkah-langkah di bawah ini:

### 1. Membuat Virtual Environment

Pastikan Anda sudah memiliki Python 3.7+ terinstal. Buatlah virtual environment untuk proyek ini agar dependensi terisolasi:

```bash
# Di macOS/Linux
python3 -m venv env

# Di Windows
python -m venv env
```

Aktifkan virtual environment:

```bash
# Di macOS/Linux
source env/bin/activate

# Di Windows
env\Scripts\activate
```

### 2. Menginstal Library yang Dibutuhkan

Setelah virtual environment aktif, instal library yang dibutuhkan dengan menggunakan file `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 3. Menjalankan Aplikasi

Untuk menjalankan dashboard, gunakan perintah berikut:

```bash
python app.py
```

Perintah ini akan menjalankan chatbot pada lokal server. Buka URL yang diberikan di browser Anda untuk mengakses chatbot.
