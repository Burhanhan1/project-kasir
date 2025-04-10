import csv

keranjang = []
file_name = fr"purchase.csv"

def header(title, separator):
    '''Membuat header untuk sebuah {prompt} yang dibatasi {separator}'''
    print("\n" + separator)
    print(title)
    print(separator)

def tampilkan_menu():
    header("MENU PROGRAM KASIR".center(55), "-" * 55)
    print("1. Tambah Barang")
    print("2. Hapus Barang")
    print("3. Lihat Keranjang")
    print("4. Hitung Total & Bayar")
    print("0. Exit")

def save_data():
    '''Menyimpan data belanja ke purchase.csv'''
    with open(file_name, mode="w", newline="") as file:
        # membuka file csv dengan mode write
        writer = csv.writer(file)
        writer.writerow(["Nama", "Jumlah", "Harga"])
        # membuat header untuk atribut item dalam keranjang
        for item in keranjang:
            writer.writerow([item["Nama"], item["Jumlah"], item["Harga"]])
            # menuliskan atribut nama, jumlah, dan harga item ke dalam file csv

def load_data():
    '''Memuat data belanja dari purchase.csv'''
    global keranjang
    # mengakses variabel keranjang sebagai variabel global
    try:
        with open(file_name, mode="r") as file:
            # membuka file csv dengan mode read
            reader = csv.DictReader(file)
            keranjang = [{"Nama": row["Nama"], "Jumlah": int(row["Jumlah"]),
                          "Harga": int(row["Harga"])} for row in reader]
            # membaca data dalam file csv untuk dieksekusi program kasir.py
    except (FileNotFoundError, ValueError):
        return

def input_str(prompt):
    '''Mengambil input str dari user'''
    while True:
        char = input(f"> {prompt}").strip()
        if not char:
            print("[Input tidak boleh kosong]")
            continue
            # ulang program jika input kosong
        else:
            return char.capitalize()
            # mengembalikan char dengan kapitalisai di huruf pertama

def input_int(prompt):
    ''''Mengambil input int dari user'''
    while True:
        try:
            number = int(input(f"> {prompt}").replace(",", "").replace(".", ""))
            if number <= 0:
                print("[Angka harus lebih dari 0]")
                # ulang program jika input kurang dari sama dengan 0
            else:
                return number
                # mengembalikan number segabai data int
        except ValueError:
            print("[Masukkan angka yang valid]")
            # ulang program jika input angka tidak valid

def find(nama):
    '''Mencari item dalam list keranjang'''
    for idx, item in enumerate(keranjang):
        if item["Nama"].lower() == nama.lower():
            return idx, item
            # mengembalikan seluruh atribut item jika nama cocok
    return None, None
    # mengembalikan nilai sebagai None jika tidak ada item dengan nama yang sesuai

def tambah_barang():
    '''Menambah item ke dalam list keranjang'''
    nama = input_str("Masukkan item baru: ")
    idx, _ = find(nama)
    if idx is not None:
        print(f"[{nama} sudah ada di dalam keranjang]")
        return
        # kembali ke menu awal jika sudah ada item dengan nama yang sama 
    jumlah = input_int("Masukkan jumlah item: ")
    harga = input_int("Masukkan harga item: ")
    keranjang.append({"Nama": nama, "Jumlah": jumlah, "Harga": harga})
    # memasukkan atribut nama, jumlah, dan harga item ke dalam list
    print(f"[{nama} ({jumlah:,} x {harga:,}) berhasil ditambahkan]")

def hapus_barang():
    '''Menghapus item di dalam list keranjang'''
    if not keranjang:
        print("[Keranjang masih kosong]")
        return
    lihat_keranjang()
    print()
    nama = input_str("Masukkan nama/nomor: ")
    idx, item = find(nama)
    if item:
        print(f"[{nama} berhasil dihapus]")
        del keranjang[idx]
        # menghapus item dengan nama yang sama di dalam list
    elif nama.isdigit() and 0 < int(nama) <= len(keranjang):
        print(f"[{keranjang[int(nama) - 1]["Nama"]} berhasil dihapus]")
        del keranjang[int(nama) - 1]
    else:
        print(f"[{nama} tidak ditemukan]")
        # kembali ke menu awal jika tidak ada item dengan nama yang sesuai

def lihat_keranjang():
    '''Menampilkan daftar belanja dalam bentuk tabel'''
    if not keranjang:
        print("[Keranjang masih kosong]")
        return
    header(f"{'No.':<5}{'Nama':<14}{'Jumlah':<8}{'Harga':<14}{'Total'}", "=" * 55)
    # membuat format tabel keranjang agar terlihat rapi
    for i, item in enumerate(keranjang, start=1):
        total = item["Harga"] * item["Jumlah"]
        # menghitung total dengan mengalikan jumlah dan harga untuk setiap item
        print(f"{i:<5}{item['Nama']:<14}{item['Jumlah']:<8,}{item['Harga']:<14,}{total:,}")
        # membuat format tabel isi keranjang agar terlihat rapi
    print("=" * 55 + "\n" + "###".center(55))

def hitung_total():
    '''Menghitung total, mengambil pembayaran, dan menghitung kembalian'''
    if not keranjang:
        print("[Keranjang masih kosong]")
        return
    total = sum(item["Harga"] * item["Jumlah"] for item in keranjang)
    # menjumlahkan semua jumlah * harga item di dalam list
    print(f"[Total belanja: {total:,}]")
    if total >= 100000:
        diskon = total * 0.1
        total -= diskon
        print("[Anda mendapatkan diskon 10%]")
        print(f"[Total yang harus dibayar: {total:,.0f}]")
        # memberikan diskon sebesar 10% jika harga total lebih dari 100000
    if input_str("Lakukan pembayaran? (y): ").lower() != "y":
        return
    bayar = input_int("Masukkan jumlah uang: ")
    while True:
        if bayar < total:
            print("[Uang tidak cukup]")
            return
            # kembali ke menu awal jika uang pembayaran tidak cukup
        else:
            print(f"[Kembalian: {bayar - total:,}]")
            print("[Terima kasih sudah berbelanja]")
            keranjang.clear()
            # menghapus semua item di dalam list setelah pembayaran berhasil
            break

def main():
    '''Menjalankan fungsi-fungsi utama dalam program kasir.py'''
    load_data()
    # load data setiap kali eksekusi fungsi main()
    while True:
        tampilkan_menu()
        print()
        fungsi = input_str("Pilih menu (0-4): ")
        pilihan = {
            "1": tambah_barang,
            "2": hapus_barang,
            "3": lihat_keranjang,
            "4": hitung_total,
        }
        # membuat dictionary untuk fungsi-fungsi utama
        if fungsi in pilihan:
            pilihan[fungsi]()
            # eksekusi fungsi jika input sesuai dengan dictionary
            save_data()
            # save data setelah menjalankan setiap fungsi
        elif fungsi in {"0", "exit", "e"}:
            print("[Program selesai]")
            break
            # keluar dari program kasir.py
        else:
            print("[Pilihan tidak tersedia]")
            # kembali ke menu utama jika tidak ada perintah yang sesuai

if __name__ == "__main__":
    main()
# eksekusi fungsi main() jika dijalankan secara langsung
# dan tidak mengeksekusi kode jika diimport sebagai module