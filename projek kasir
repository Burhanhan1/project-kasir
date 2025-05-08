keranjang = []

def tampilkan_menu():
    print("\n=== APLIKASI KASIR SEDERHANA ===")
    print("1. Tambah Barang")
    print("2. Lihat Keranjang")
    print("3. Hitung Total Harga")
    print("4. Keluar")

def tambah_barang():
    nama = input("Masukkan nama barang: ")
    try:
        harga = int(input("Masukkan harga barang: Rp "))
        keranjang.append({"nama": nama, "harga": harga})
        print(f"Barang '{nama}' berhasil ditambahkan.")
    except ValueError:
        print("Harga harus berupa angka bulat.")

def lihat_keranjang():
    if not keranjang:
        print("Keranjang kosong.")
    else:
        print("\nIsi Keranjang:")
        for idx, item in enumerate(keranjang, start=1):
            print(f"{idx}. {item['nama']} - Rp {item['harga']}")

def hitung_total():
    total = sum(item["harga"] for item in keranjang)
    print(f"\nTotal Harga: Rp {total}")
    if total > 100000:
        diskon = total * 0.10
        total_diskon = total - diskon
        print(f"Diskon 10%: Rp {int(diskon)}")
        print(f"Total Setelah Diskon: Rp {int(total_diskon)}")
    else:
        print("Diskon tidak berlaku (Minimal belanja Rp100.000).")

# Program utama
while True:
    tampilkan_menu()
    pilihan = input("Pilih opsi (1-4): ")
    
    if pilihan == "1":
        tambah_barang()
    elif pilihan == "2":
        lihat_keranjang()
    elif pilihan == "3":
        hitung_total()
    elif pilihan == "4":
        print("Terima kasih telah menggunakan aplikasi kasir.")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih antara 1-4.")
