#Data_Pilihan_Rumah
rumah_list = [
    ["Rumah A", "Kota", "ramai", 3, 800_000_000],
    ["Rumah B", "Pinggiran", "sepi", 4, 600_000_000],
    ["Rumah C", "Kota", "sepi", 2, 700_000_000]
]

lanjut = "iya"
while lanjut != "gak":
    print("===================================")
    print("PickaHome: Sistem Rekomendasi Rumah")
    print("===================================")
    Tipe_User = input("Kamu itu seller atau buyer?:  ")
    if Tipe_User == "seller":
        Rumah_add = input("Silakah masukan rumah yang mau di jual dengan Format: [nama, lokasi, suasana, kamar, harga]: ")
        rumah_list.append(Rumah_add)
        print(rumah_list)

    if Tipe_User == "buyer":
        #User_Input_Prefensi_Mereka
        print("=== Silahkan masukan prefensi rumah anda ===")
        Jumlah_kamar = int(input("Berapa jumlah kamar yang dibutuhkan? "))
        suasana = input("Suka lingkungan sepi atau ramai? ").lower()
        lokasi = input("Mau di area mana? (Kota/Pinggiran) ").capitalize()
        Harga = int(input("hargany sekitar berapa? = "))

        rekomendasi = []

        # Loop semua rumah dan mendefinisikan tiap komponen dalam list
        for rumah in rumah_list:
            if rumah[2] == suasana and rumah[1] == lokasi and rumah[3] >= Jumlah_kamar and rumah[4]<=Harga: 
                rekomendasi.append(rumah)

        # Menampilkan hasilnya
        if len(rekomendasi) > 0:
            print("Rekomendasi rumah untukmu:")
            for r in rekomendasi:
                 print(f"- {r[0]} ({r[1]}, suasana {r[2]}, {r[3]} kamar, harga Rp{r[4]:,})")

        else:
            print("Maaf, belum ada rumah yang cocok dengan preferensimu.")
        
        lanjut = input("mau lanjutin sistemnya atau gak (iya atau gak)").lower()
        
print("=========================================")
print("Terima kasih telah menggunakan sistem ini")
print("=========================================")


