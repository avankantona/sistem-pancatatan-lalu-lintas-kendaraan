# Sistem Pencatatan Lalu Lintas Kendaraan

## Deskripsi

Project ini dibuat untuk membantu pencatatan lalu lintas kendaraan yang dilakukan oleh petugas polisi pada suatu lokasi tertentu. Program dibuat menggunakan Python dan berjalan melalui terminal (CLI).

Sebelum melakukan pencatatan, petugas terlebih dahulu memilih identitas polisi yang bertugas dan lokasi tempat bertugas. Setelah itu petugas dapat melakukan input jumlah kendaraan yang melintas secara cepat maupun secara manual.

Selain itu, tersedia menu master data untuk mengelola data kendaraan, lokasi, dan polisi.

## Tujuan

Tujuan dari dibuatnya sistem ini adalah untuk membantu proses pencatatan lalu lintas kendaraan secara lebih terstruktur dan memudahkan petugas dalam mengumpulkan data kepadatan kendaraan pada setiap lokasi pengamatan.

Data yang diperoleh dapat digunakan untuk:

* Mengetahui tingkat kepadatan lalu lintas pada jalan raya tertentu.
* Mengidentifikasi titik-titik yang sering mengalami kemacetan.
* Membandingkan volume kendaraan antar lokasi.
* Menjadi bahan evaluasi dan pengambilan keputusan terkait pengaturan lalu lintas.
* Mempermudah proses pencatatan kendaraan oleh petugas di lapangan.

---

## Fitur

### Input Lalu Lintas Cepat

Digunakan untuk pencatatan kendaraan satu per satu. Setiap input akan otomatis memiliki jumlah kendaraan sebanyak 1 dan waktu pencatatan akan tersimpan secara otomatis.

### Input Lalu Lintas Banyak

Digunakan apabila terdapat beberapa kendaraan dengan jenis yang sama. Petugas dapat menentukan jumlah kendaraan secara langsung.

### Lihat Data Transaksi

Menampilkan seluruh data transaksi lalu lintas yang sudah tercatat.

### Ganti Petugas

Digunakan untuk memilih polisi yang bertugas dan lokasi tempat bertugas.

### Master Data

Master data terdiri dari:

* Data Kendaraan
* Data Lokasi
* Data Polisi

Setiap master data memiliki fitur:

* Lihat data
* Tambah data
* Hapus data

---

## Struktur Data

### Kendaraan

* jenis_id
* jenis_kendaraan

### Lokasi

* lokasi_id
* nama_lokasi

### Polisi

* polisi_id
* nama_polisi
* tempat_dinas

### Transaksi

* transaksi_id
* polisi_id
* lokasi_id
* jenis_id
* qty
* waktu

---

## Cara Menjalankan Program

Pastikan Python sudah terinstall.

Jalankan program dengan perintah:

```bash
python 001_avan_capstone.py
```

---

## Menu Utama

```
1. Input Cepat
2. Input Banyak
3. Lihat Transaksi
4. Ganti Petugas
5. Master Data
0. Keluar
```

---

## Teknologi yang Digunakan

* Python 3
* Module time
* Module datetime

---

## Catatan

Data pada program masih disimpan menggunakan list dan dictionary sehingga data akan kembali ke kondisi awal ketika program ditutup. Project ini dibuat sebagai Capstone Project Modul 1 Purwadhika dan berfokus pada penerapan dasar Python seperti:

* Function
* Looping
* Conditional
* List
* Dictionary
* Exception Handling
* CRUD sederhana
* Modular Programming
