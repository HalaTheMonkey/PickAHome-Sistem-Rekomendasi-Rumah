# Projek PickAHome: Smart House Recommendation System
# Deskripsi: Program yang menyediakan wadah untuk membeli dan menjual rumah

# Variabel
# rumah_list: list
# lanjut: string
# Tipe_User: string

# Data pilihan rumah
list_rumah = [
    ["Rumah A", "Kota", "ramai", 3, 800_000_000, "Jl. Venus No. 90, RT 004/RW 006, Kel. Mekar Sari, Kec. Sukamaju, Kota Bandung, Jawa Barat 40291", "0811234678" ],
    ["Rumah B", "Pinggiran", "sepi", 4, 600_000_000, "Jl. Anggrek Raya No. 27, RT 002/RW 009, Kel. Karang Tengah, Kec. Cipondoh, Kota Tangerang, Banten 15157" , "08112346799" ],
    ["Rumah C", "Kota", "sepi", 2, 700_000_000, "Jl. Melati Indah No. 135, RT 005/RW 003, Desa Sidomulyo, Kec. Banyudono, Kab. Boyolali, Jawa Tengah 57373", "0811234678876"]
]

# Looping agar program tetap berjalan
lanjut = "iya"
while lanjut != "tidak":
    print("===================================")
    print("PickaHome: Sistem Rekomendasi Rumah")
    print("===================================")
    Tipe_User = input("Ingin memilih sebagai buyer atau seller? ")
    print()
    
    if Tipe_User == "seller":
        print("=== Silahkan input data rumah yang ingin dijual ===")
        # Seller mengisi data rumah yang akan dijual dan diisi dalam list
        Rumah_add = []
        Nama_add = input("Masukkan nama rumah yang dijual: ").title()
        Rumah_add.append(Nama_add)

        lokasi = input("Lokasi rumah di Kota atau Pinggiran? ").capitalize()
        Rumah_add.append(lokasi)

        suasana_add = input("Suasana pada sekitar rumah bagaimana? (sepi/ramai): ").lower()
        Rumah_add.append(suasana_add)

        Jumlah_kamar_add = int(input("Masukkan jumlah kamar pada rumah: "))
        Rumah_add.append(Jumlah_kamar_add)

        Harga_add = int(input("Range harga yang ingin diberikan: "))
        Rumah_add.append(Harga_add)

        NomorTelpon_add = input("Masukan nomor telpon anda: ")
        Rumah_add.append(NomorTelpon_add)

        AlamatLengkap_add = input("Masukan Alamat Lengkap rumah (co: Jl. Melati Indah No. 135, RT 005/RW 003, Desa Sidomulyo, Kec. Banyudono, Kab. Boyolali, Jawa Tengah 57373: ")
        Rumah_add.append(AlamatLengkap_add)
        
        list_rumah.append(Rumah_add)
        print()

    if Tipe_User == "buyer":
        # Buyer memilih prefensi rumah
        print("=== Silahkan input prefensi rumah anda ===")
        Jumlah_kamar = int(input("Berapa jumlah kamar yang dibutuhkan? "))
        suasana = input("Suka lingkungan sepi atau ramai? ").lower()
        lokasi = input("Mau di area mana? (Kota/Pinggiran): ").capitalize()
        Harga = int(input("Range harga yang diinginkan? "))
        print()

        rekomendasi = []

        # Loop semua rumah dan mendefinisikan tiap komponen dalam list
        for rumah in list_rumah:
            if rumah[2] == suasana and rumah[1] == lokasi and rumah[3] >= Jumlah_kamar and rumah[4]<=Harga: 
                rekomendasi.append(rumah)

        # Menampilkan hasilnya
        if len(rekomendasi) > 0:
            print("Rekomendasi rumah untukmu:")
            for r in rekomendasi:
                 print(f"- {r[0]} ({r[1]}, suasana {r[2]}, {r[3]} kamar, harga Rp{r[4]:,}, alamat rumah: {r[5]}, nomor telefon pemilik: {r[6]})")

        else:
            print("Maaf, belum ada rumah yang cocok dengan preferensimu.")
        print()

        lanjut = input("Apakah sistem ingin dilanjutkan? (iya/tidak)").lower()
        print()
        
print("=========================================")
print("Terima kasih telah menggunakan sistem ini")
print("=========================================")


