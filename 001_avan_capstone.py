import time
from datetime import datetime

welcome_txt                                             = "Selamat datang di Sistem Pencatatan Lalu Lintas Kendaraan\n"

ar_kendaraan = [
    {"jenis_id": 1, "jenis_kendaraan": "Roda dua"},
    {"jenis_id": 2, "jenis_kendaraan": "Roda empat"},
    {"jenis_id": 3, "jenis_kendaraan": "Bus"},
    {"jenis_id": 4, "jenis_kendaraan": "Truck"},
]

ar_lokasi = [
    {"lokasi_id": 1, "nama_lokasi": "Terminal Pulo Gebang"},
    {"lokasi_id": 2, "nama_lokasi": "Pasar Senen"},
    {"lokasi_id": 3, "nama_lokasi": "Puncak"},
]

ar_polisi = [
    {"polisi_id": 1, "nama_polisi": "Avan", "tempat_dinas": "Buaran"},
    {"polisi_id": 2, "nama_polisi": "Kantona", "tempat_dinas": "Bogor"},
]

ar_transaksi = []

polisi_aktif                                            = None
lokasi_aktif                                            = None


def pilih_petugas():

    global polisi_aktif
    global lokasi_aktif

    print("\n=== PILIH POLISI ===")
    for item in ar_polisi:
        print(item["polisi_id"], item["nama_polisi"])

    polisi_aktif = int(input("Pilih polisi ID: "))

    print("\n=== PILIH LOKASI ===")
    for item in ar_lokasi:
        print(item["lokasi_id"], item["nama_lokasi"])

    lokasi_aktif = int(input("Pilih lokasi ID: "))


def input_lalulintas_cepat():

    print("\n=== INPUT CEPAT ===")

    while True:

        for item in ar_kendaraan:
            print(item["jenis_id"], item["jenis_kendaraan"])

        print("\nKetik selain ID untuk selesai")

        try:
            jenis = int(input("Pilih jenis kendaraan: "))
        except:
            print("Input harus angka!")
            continue

        valid = any(item["jenis_id"] == jenis for item in ar_kendaraan)

        if valid:

            data = {
                "transaksi_id"                                  : len(ar_transaksi) + 1,
                "polisi_id"                                     : polisi_aktif,
                "lokasi_id"                                     : lokasi_aktif,
                "jenis_id"                                      : jenis,
                "qty"                                           : 1,
                "waktu"                                         : datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }

            ar_transaksi.append(data)
            print("Berhasil input cepat!")

        else:
            print("Selesai input cepat...")
            break

def input_lalulintas_banyak():

    print("\n=== INPUT BANYAK ===")

    for item in ar_kendaraan:
        print(item["jenis_id"], item["jenis_kendaraan"])

    try:
        jenis = int(input("Pilih jenis kendaraan: "))
        qty = int(input("Masukkan jumlah kendaraan: "))
    except:
        print("Input harus angka!")
        return

    data = {
        "transaksi_id"                                  : len(ar_transaksi) + 1,
        "polisi_id"                                     : polisi_aktif,
        "lokasi_id"                                     : lokasi_aktif,
        "jenis_id"                                      : jenis,
        "qty"                                           : qty,
        "waktu"                                         : datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    ar_transaksi.append(data)
    print("Berhasil input banyak!")


def lihat_transaksi():

    print("\n=== DATA TRANSAKSI ===")

    tampil_tabel(ar_transaksi)


def master_data():

    ar_master = [
        {"id": 1, "nama": "Kendaraan", "data": ar_kendaraan},
        {"id": 2, "nama": "Lokasi", "data": ar_lokasi},
        {"id": 3, "nama": "Polisi", "data": ar_polisi}
    ]

    while True:

        print("\n=== MASTER DATA ===")

        for item in ar_master:
            print(f"{item['id']}. {item['nama']}")

        print("0. Kembali")

        try:
            master = int(input("Pilih data: "))
        except:
            print("Harus angka!")
            continue

        if master == 0:
            break

        for item in ar_master:
            if item["id"] == master:

                crud_master(item["data"], item["nama"])

def crud_master(data, nama):
    while True:
        print(f"\n=== CRUD {nama.upper()} ===")
        print("1. Lihat")
        print("2. Tambah")
        print("3. Hapus")
        print("0. Kembali")

        pilih = input("Pilih menu: ")

        if pilih == "1":
            tampil_tabel(data)

        elif pilih == "2":

            ar_insert = {}

            for field in data[0]:

                while True:

                    value = input(f"Masukkan {field}: ")

                    try:
                        if isinstance(data[0][field], int):
                            value = int(value)

                        ar_insert[field] = value
                        break

                    except:
                        print("Input salah!")

            key_id = list(data[0].keys())[0]
            ar_insert[key_id] = len(data) + 1

            data.append(ar_insert)
            print("Berhasil tambah data!")

        elif pilih == "3":

            tampil_tabel(data)

            try:
                hapus = int(input("Masukkan ID yang dihapus: "))
            except:
                print("Harus angka!")
                continue

            key_id = list(data[0].keys())[0]

            for item in data:
                if item[key_id] == hapus:
                    data.remove(item)
                    print("Berhasil hapus!")
                    break

        elif pilih == "0":
            break

        else:
            print("Menu tidak valid")

def tampil_tabel(data):

    if len(data) == 0:
        print("Data kosong")
        return

    headers = list(data[0].keys())

    print("\nIndex     | " + " | ".join(f"{h.capitalize():<12}" for h in headers))
    print("-" * 70)

    for i, item in enumerate(data):
        row = f"{i:<9} | "

        for h in headers:
            row += f"{str(item[h]):<12} | "

        print(row)


def menu():

    print("\n1. Input Cepat")
    print("2. Input Banyak")
    print("3. Lihat Transaksi")
    print("4. Ganti Petugas")
    print("5. Master Data")
    print("0. Keluar")


def main():

    print(welcome_txt)

    pilih_petugas()

    while True:

        menu()

        user_input                                          = input("\nMasukkan menu: ")

        print("Pilihan Anda =", user_input)
        time.sleep(1)

        if user_input == "1":
            input_lalulintas_cepat()

        elif user_input == "2":
            input_lalulintas_banyak()

        elif user_input == "3":
            lihat_transaksi()

        elif user_input == "4":
            pilih_petugas()

        elif user_input == "5":
            master_data()

        elif user_input == "0":
            print("Program selesai")
            break

        else:
            print("Menu tidak valid")

        input("\nTekan Enter untuk lanjut...")


main()