
#list pelanggan
pelanggan = {1211: "Ronaldo", 1212: "Messi", 1213: "Tom Brady"}


#list barang
barang = [
    "Tempe", "Tahu", "Kangkung", "Bayam", "Daging", "Roti", "Tepung",
    "Telur", "Ayam Goreng", "Pasta Gigi", "Mainan Mobil", "Mi Instan" 
]


#list harga
harga = {
    "Tempe": 3000,
    "Tahu" : 2000,
    "Kangkung" : 1500,
    "Bayam" : 2500,
    "Daging" : 110000,
    "Roti" : 15000,
    "Tepung" : 6000,
    "Telur" : 35000,
    "Ayam Goreng" : 20000,
    "Pasta Gigi" : 15000,
    "Mainan Mobil" : 200000,
    "Mi Instan" : 3000

}


#membuat keranjang kosong
keranjang = []
jumlah_belanja = []
harga_belanja = []
count_total_harga = 0
bayar = True


class Transaction:
    def __init__(self, ID):
        self.ID = ID

#alur awal berbelanja
def start_belanja():
    try:
        id_transaction = int(input("Masukkan ID toko kamu: "))
        trnsct_123 = Transaction(id_transaction)
        print(f"ID toko kamu adalah {trnsct_123.ID}")
        print(f"Selamat datang {pelanggan[trnsct_123.ID]}! Silakan berbelanja")
    except KeyError:
        raise KeyError ("Mohon maaf ID tidak terdaftar")
    except ValueError:
        raise ValueError ("Masukkan ID yang benar, mohon ulangi proses")



#alur main menu
def main_menu():
    print(''' 
SELAMAT DATANG DI TOKO KAMI

Pilih Opsi Berikut:
1. Menambahkan Barang
2. Ganti Barang
3. Hapus Barang
4. Cek Keranjang Belanja
5. Bayar

0. Exit
''')
    opsi = int(input("Silakan masukkan opsi angka: ") )
    try:
        if opsi == 0 and bayar == True:
            print("Terima kasih sudah berkunjung!")
    
        elif opsi == 0 and bayar == False:
            print("Mohon melakukan pembayaran terlebih dahulu")
            return main_menu()

        elif opsi == 1:
            tambah_barang()

        elif opsi == 2:
            print('''
        UPDATE BARANG
        
        Pilih opsi:
        1. Ganti jenis barang
        2. Ganti jumlah barang

        0. Kembali
        ''')
            opsi_update = int(input("Silakan masukkan opsi angka: "))
            try:
                if opsi_update == 1:
                    update_barang()
                elif opsi_update == 2:
                    update_jumlah()
                elif opsi_update == 0:
                    return main_menu()
                else:
                    print("Opsi invalid, kembali ke main menu")
                    return main_menu()
            except ValueError:
                raise ValueError ("Masukkan opsi yang benar, mohon ulangi proses")

        elif opsi == 3:
            print('''
        HAPUS BARANG
        
        Pilih opsi:
        1. Hapus sebagian
        2. Hapus seluruhnya

        0. Kembali
        ''')

            opsi_hapus = int(input("Silakan masukkan opsi angka: "))
            try:
                if opsi_hapus == 1:
                    hapus_barang()
                elif opsi_hapus == 2:
                    reset_barang()
                elif opsi_hapus == 0:
                    return main_menu()
                else:
                    print("Opsi invalid, kembali ke main menu")
                    return main_menu()
            except ValueError:
                raise ValueError ("Masukkan opsi yang benar, mohon ulangi proses")

        elif opsi == 4:
            cek_keranjang()
    
        elif opsi == 5:
            pembayaran()
    
    except ValueError:
        raise ValueError ("Masukkan opsi yang benar, mohon ulangi proses")

    


#method menambahkan barang
def tambah_barang():
    print('''
SILAKAN PILIH BARANG
(harga per pcs/kg)

0. Tempe = Rp 3.000
1. Tahu = Rp 2.000
2. Kangkung = Rp 1.500
3. Bayam = Rp 2.500
4. Daging = Rp 110.000
5. Roti = Rp 15.000
6. Tepung = Rp 6.000
7. Telur = Rp 35.000,
8. Ayam Goreng = Rp 20.000
9. Pasta Gigi = Rp 15.000
10. Mainan Mobil = Rp 200.000
11. Mi Instan = Rp 3.000

99. Kembali ke menu utama

''')
    belanjaan = int(input("Silakan pilih nomor barangnya: "))
    if belanjaan == 99:
        print("Kembali ke main menu")
        main_menu()
    else: 
        nama_barang = barang[belanjaan]
        jumlah_barang = int(input("Anda ingin membeli berapa buah? "))
        harga_barang = jumlah_barang * harga[barang[belanjaan]]
        konfirmasi = input(f"Apakah anda yakin ingin membeli {nama_barang} sebanyak {jumlah_barang} buah? (Yes/No)")

        if konfirmasi == 'Yes' or konfirmasi == 'YES' or konfirmasi == 'yes':
            print(f"Berhasil beli {nama_barang}, sebanyak {jumlah_barang} buah, dengan harga {harga_barang}")
            keranjang.append (barang[belanjaan])
            jumlah_belanja.append (jumlah_barang)
            harga_belanja.append (harga_barang)
            global count_total_harga
            count_total_harga = count_total_harga + harga_barang
            global bayar
            bayar = False
            return tambah_barang()
    
    
        elif konfirmasi == 'No' or konfirmasi == 'NO' or konfirmasi == 'no':
            print("Pilihan dibatalkan, kembali pilih barang")
            return tambah_barang()

        else: 
            print("Pilihan invalid, kembali pilih barang")
            return tambah_barang()



#Update barang
def update_barang():
    if keranjang == []:
        print("Keranjang belanja kosong, mohon diisi dahulu")
        main_menu()
    else:
        print("KERANJANG BELANJA")
        for indexlist in range (0, len(keranjang)):
            print(f'''
            {indexlist}. {keranjang[indexlist]}''')
    
        index_update_barang = int(input("Pilih nomor barang yang akan diubah: "))
        global count_total_harga
        count_total_harga = count_total_harga - harga_belanja[index_update_barang]

        print(f"Barang {keranjang[index_update_barang]} akan diubah")
        print('''
SILAKAN PILIH BARANG
(harga per pcs/kg)

0. Tempe = Rp 3.000
1. Tahu = Rp 2.000
2. Kangkung = Rp 1.500
3. Bayam = Rp 2.500
4. Daging = Rp 110.000
5. Roti = Rp 15.000
6. Tepung = Rp 6.000
7. Telur = Rp 35.000,
8. Ayam Goreng = Rp 20.000
9. Pasta Gigi = Rp 15.000
10. Mainan Mobil = Rp 200.000
11. Mi Instan = Rp 3.000

99. Kembali
''')
        belanjaan = int(input("Silakan pilih nomor barangnya: "))
        if belanjaan == 99:
            print("Kembali ke main menu")
            main_menu()
        else: 
            nama_barang = barang[belanjaan]
            jumlah_barang = int(input("Anda ingin membeli berapa buah? "))
            harga_barang = jumlah_barang * harga[barang[belanjaan]]
            konfirmasi = input(f"Apakah anda yakin ingin membeli {nama_barang} sebanyak {jumlah_barang} buah? (Yes/No)")

            if konfirmasi == 'Yes' or konfirmasi == 'YES' or konfirmasi == 'yes':
                print(f"Berhasil beli {nama_barang}, sebanyak {jumlah_barang} buah, dengan harga {harga_barang}")
                keranjang[index_update_barang] = (barang[belanjaan])
                jumlah_belanja[index_update_barang] = (jumlah_barang)
                harga_belanja[index_update_barang] = (harga_barang)
                #global count_total_harga
                count_total_harga = count_total_harga + harga_barang
                main_menu()
    
    
            elif konfirmasi == 'No' or konfirmasi == 'NO' or konfirmasi == 'no':
                print("Pilihan dibatalkan, kembali ke main menu")
                return main_menu()

            else: 
                print("Pilihan invalid, kembali ke main menu")
                return main_menu()



#Update jumlah
def update_jumlah():
    if keranjang == []:
        print("Keranjang belanja kosong, mohon diisi dahulu")
        main_menu()
    else:
        print("KERANJANG BELANJA")
        for indexlist in range (0, len(keranjang)):
            print(f'''
            {indexlist}. {keranjang[indexlist]} berjumlah {jumlah_belanja[indexlist]}''')
        index_update_jumlah = int(input("Pilih nomor barang yang akan diubah: "))
        global count_total_harga
        count_total_harga = count_total_harga - harga_belanja[index_update_jumlah]     

        nama_barang = keranjang[index_update_jumlah]
        jumlah_barang = int(input("Anda ingin membeli berapa buah? "))
        harga_barang = jumlah_barang * harga[keranjang[index_update_jumlah]]
        konfirmasi = input(f"Apakah anda yakin ingin membeli {nama_barang} sebanyak {jumlah_barang} buah? (Yes/No)")

        if konfirmasi == 'Yes' or konfirmasi == 'YES' or konfirmasi == 'yes':
            print(f"Berhasil beli {nama_barang}, sebanyak {jumlah_barang} buah, dengan harga {harga_barang}")
            jumlah_belanja[index_update_jumlah] = (jumlah_barang)
            harga_belanja[index_update_jumlah] = (harga_barang)
            #global count_total_harga
            count_total_harga = count_total_harga + harga_barang
            main_menu()
    
    
        elif konfirmasi == 'No' or konfirmasi == 'NO' or konfirmasi == 'no':
            print("Pilihan dibatalkan, kembali ke main menu")
            return main_menu()

        else: 
            print("Pilihan invalid, kembali ke main menu")
            return main_menu()



#Hapus barang
def hapus_barang():
    if keranjang == []:
        print("Keranjang belanja kosong, mohon diisi dahulu")
        main_menu()
    else:
        print("KERANJANG BELANJA")
        for indexlist in range (0, len(keranjang)):
            print(f'''
            {indexlist}. {keranjang[indexlist]} berjumlah {jumlah_belanja[indexlist]}''')
        index_hapus_barang = int(input("Pilih nomor barang yang akan dihapus: "))
        konfirmasi = input(f"Apakah anda yakin ingin menghapus {keranjang[index_hapus_barang]} sebanyak {jumlah_belanja[index_hapus_barang]} buah? (Yes/No)")

        if konfirmasi == 'Yes' or konfirmasi == 'YES' or konfirmasi == 'yes':
            print(f"Berhasil menghapus {keranjang[index_hapus_barang]}, sebanyak {jumlah_belanja[index_hapus_barang]} buah, dengan harga {harga_belanja[index_hapus_barang]}")
            global count_total_harga
            count_total_harga = count_total_harga - harga_belanja[index_hapus_barang]

            keranjang.pop(index_hapus_barang)
            jumlah_belanja.pop(index_hapus_barang)
            harga_belanja.pop(index_hapus_barang)
            if keranjang == []:
                global bayar
                bayar = True

            print("Kembali ke main menu")
            return main_menu()
    
        elif konfirmasi == 'No' or konfirmasi == 'NO' or konfirmasi == 'no':
            print("Pilihan dibatalkan, kembali ke main menu")
            return main_menu()

        else: 
            print("Pilihan invalid, kembali ke main menu")
            return main_menu()
        




#Reset barang
def reset_barang():
        if keranjang == []:
            print("Keranjang belanja kosong, mohon diisi dahulu")
            main_menu()
        else:
            print("KERANJANG BELANJA")
            for indexlist in range (0, len(keranjang)):
                print(f'''
                {indexlist}. {keranjang[indexlist]} berjumlah {jumlah_belanja[indexlist]}''')
            konfirmasi = input(f"Apakah anda yakin ingin menghapus seluruh barang? (Yes/No)")

        if konfirmasi == 'Yes' or konfirmasi == 'YES' or konfirmasi == 'yes':
            print(f"Berhasil menghapus seluruh barang")
            global count_total_harga
            count_total_harga = 0

            keranjang.clear()
            jumlah_belanja.clear()
            harga_belanja.clear()
            global bayar
            bayar = True

            print("Kembali ke main menu")
            return main_menu()
    
        elif konfirmasi == 'No' or konfirmasi == 'NO' or konfirmasi == 'no':
            print("Pilihan dibatalkan, kembali ke main menu")
            return main_menu()

        else: 
            print("Pilihan invalid, kembali ke main menu")
            return main_menu()



#Cek Keranjang Belanja
def cek_keranjang():
    print(f'''
        KERANJANG BELANJA
''')
    if keranjang == []:
        print("Keranjang belanja kosong, mohon diisi dahulu")
        main_menu()
    else:   
        for indexlist in range (0, len(keranjang)):
            print(f'''
-- {keranjang[indexlist]} berjumlah {jumlah_belanja[indexlist]} buah/kg dengan total harga Rp {harga_belanja[indexlist]}
        ''')
        
        print(f"Total harga seluruhnya adalah {count_total_harga}")
        print("Kembali ke main menu")
        main_menu()



#Pembayaran
def pembayaran():
    print(f'''
        KERANJANG BELANJA
''')
    global count_total_harga
    if keranjang == []:
        print("Keranjang belanja kosong, tidak perlu pembayaran apapun")
        main_menu()
    else:
        for indexlist in range (0, len(keranjang)):
            print(f'''
            {indexlist}. {keranjang[indexlist]} berjumlah {jumlah_belanja[indexlist]}''')
        
        print(f"Total pembayaran adalah Rp {count_total_harga}")

        if count_total_harga > 500000:
            count_total_harga *= 0.90
            print(f"Selamat anda mendapatkan diskon 10%, total belanja menjadi Rp {count_total_harga}")
        elif count_total_harga > 300000:
            count_total_harga *= 0.92
            print(f"Selamat anda mendapatkan diskon 8%, total belanja menjadi Rp {count_total_harga}")
        elif count_total_harga > 200000:
            count_total_harga *= 0.95
            print(f"Selamat anda mendapatkan diskon 5%, total belanja menjadi Rp {count_total_harga}")

        konfirmasi = input(f"Apakah anda yakin ingin melakukan pembayaran? (Yes/No)")

        if konfirmasi == 'Yes' or konfirmasi == 'YES' or konfirmasi == 'yes':
            print(f"Berhasil melakukan pembayaran sebesar Rp {count_total_harga}. Terima kasih atas uangnya")
            count_total_harga = 0

            keranjang.clear()
            jumlah_belanja.clear()
            harga_belanja.clear()

            global bayar
            bayar = True

            print("Kembali ke main menu")
            return main_menu()
    
        elif konfirmasi == 'No' or konfirmasi == 'NO' or konfirmasi == 'no':
            print("Pilihan dibatalkan, kembali ke main menu")
            return main_menu()

        else: 
            print("Pilihan invalid, kembali ke main menu")
            return main_menu()

