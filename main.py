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
    """Menampilkan semua catatan belajar secara rapi.

    Jika belum ada catatan, tampilkan pesan yang sesuai.
    """
    print("\n--- Daftar Catatan Belajar ---")
    if not catatan:
        print("Belum ada catatan. Tambahkan catatan belajar dulu.")
        return

    for i, c in enumerate(catatan, start=1):
        mapel = c.get('mapel', '')
        topik = c.get('topik', '')
        durasi = c.get('durasi', 0)
        print(f"{i}. {mapel} - {topik} ({durasi} menit)")

    print(f"\nTotal catatan: {len(catatan)}")

def total_waktu():
    """Menghitung total durasi semua catatan dan menampilkannya.

    Menampilkan hasil dalam menit, dan juga konversi ke jam+menit jika >= 60 menit.
    """
    print("\n--- Total Waktu Belajar ---")
    if not catatan:
        print("Belum ada catatan. Tambahkan catatan belajar dulu.")
        return 0

    total = sum(c.get('durasi', 0) for c in catatan)
    jam = total // 60
    menit = total % 60

    if jam > 0:
        print(f"Total waktu belajar: {total} menit ({jam} jam {menit} menit)")
    else:
        print(f"Total waktu belajar: {total} menit")

    return total

# Target harian (disimpan dalam menit). None berarti belum diset.
target_harian = None

def set_target_harian():
    """Mengatur target harian dalam menit."""
    print("\n--- Set Target Harian ---")
    while True:
        target_input = input("Masukkan target harian (menit), kosong untuk batal: ").strip()
        if target_input == "":
            print("Pengaturan target dibatalkan.")
            return
        try:
            target = int(target_input)
            if target <= 0:
                print("Masukkan angka positif untuk target.")
                continue
            break
        except ValueError:
            print("Input tidak valid. Masukkan angka bulat (mis. 60).")

    global target_harian
    target_harian = target
    jam = target_harian // 60
    menit = target_harian % 60
    if jam > 0:
        print(f"Target harian diset: {target_harian} menit ({jam} jam {menit} menit) ✅")
    else:
        print(f"Target harian diset: {target_harian} menit ✅")


def lihat_target():
    """Menampilkan target harian saat ini dan progres terhadap total waktu yang ada.

    Catatan: Aplikasi ini tidak menyimpan tanggal, jadi progres dihitung dari semua catatan yang ada.
    """
    print("\n--- Target Harian ---")
    if target_harian is None:
        print("Belum ada target harian. Gunakan opsi 'Set Target Harian' untuk menambah target.")
        return

    total = sum(c.get('durasi', 0) for c in catatan)
    jam_t = target_harian // 60
    menit_t = target_harian % 60
    jam = total // 60
    menit = total % 60

    print(f"Target: {target_harian} menit ({jam_t} jam {menit_t} menit)")
    print(f"Total saat ini: {total} menit ({jam} jam {menit} menit)")

    if total >= target_harian:
        print("Selamat! Target harian tercapai 🎉")
    else:
        sisa = target_harian - total
        persen = int((total * 100) / target_harian) if target_harian > 0 else 0
        print(f"Sisa: {sisa} menit lagi ({persen}% tercapai)")


def menu():
    print("\n=== Study Log App ===")
    print("1. Tambah catatan belajar")
    print("2. Lihat catatan belajar")
    print("3. Total waktu belajar")
    print("4. Keluar")
    print("5. Set target harian")
    print("6. Lihat target harian")

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
    elif pilihan == "5":
        set_target_harian()
    elif pilihan == "6":
        lihat_target()
    else:
        print("Pilihan tidak valid")