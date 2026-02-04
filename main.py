catatan = []

def tambah_catatan():
    """Meminta input mapel, topik, dan durasi (menit) lalu menyimpan ke list `catatan`.
    Struktur data: list berisi dict sederhana untuk kemudahan pemahaman pemula.
    """
    print("\n--- Tambah Catatan Belajar ---")
    mapel = input("Mapel: ").strip()
    topik = input("Topik: ").strip()

    # Validasi durasi agar berupa bilangan bulat positif
    while True:
        durasi_input = input("Durasi (menit): ").strip()
        if durasi_input == "":
            print("Durasi tidak boleh kosong. Masukkan angka dalam menit.")
            continue
        try:
            durasi = int(durasi_input)
            if durasi <= 0:
                print("Masukkan angka positif untuk durasi.")
                continue
            break
        except ValueError:
            print("Input tidak valid. Masukkan angka bulat (mis. 30).")

    # Simpan catatan sebagai dict sederhana
    catatan.append({
        'mapel': mapel,
        'topik': topik,
        'durasi': durasi
    })

    print("Catatan berhasil ditambahkan ✅")

def lihat_catatan():
    pass

def total_waktu():
    pass

def menu():
    print("\n=== Study Log App ===")
    print("1. Tambah catatan belajar")
    print("2. Lihat catatan belajar")
    print("3. Total waktu belajar")
    print("4. Keluar")

while True:
    menu()
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tambah_catatan()
    elif pilihan == "2":
        lihat_catatan()
    elif pilihan == "3":
        total_waktu()
    elif pilihan == "4":
        print("Terima kasih, terus semangat belajar!")
        break
    else:
        print("Pilihan tidak valid")