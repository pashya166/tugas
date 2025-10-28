# #latihan 1
# #list number
# number = [7,5,4,3,8,9,1]

# #variabel simpan jumlah
# sum = 0

# #literasi
# for each in number:
#     sum = sum + each

# #output
# print("jumlah semuanya:", sum)

# #latihan 2
# mapel = ['matematika', 'bahasa inggris', 'PKN']

# #literasi dengan indeks
# for i in range(len(mapel)):
#     print("saya suka", mapel[i])

# #latihan 3
# count = 0
# while (count < 5):
#     print("the count is", count)
#     count = count + 1
# print("Goodbye hitam")

# #latihan 4
# count = 0
# while (count < 5):
#     print("the count is:", count)
#     count = count
# print("Goodbye Hitam")

# #latihan 5
# # menggunakan break
# for letter in "PythonProgramming":
#     if letter == "g":
#         break
#     print("Huruf sekarang:", letter)
# print("Goodbye Hitam")

# # menggunakan continue
# for letter in "PythonProgramming":
#     if letter == "g":
#         continue
#     print("Huruf sekarang:", letter)
# print("Goodbye Hitam")

# #latihan 6
# count = 0
# while (count < 8):
#     print(count, "kurang dari 8")
#     count = count + 1
# else:
#     print(count, "tidak kurang dari 8")

#Latihan soal
# ulang = 2
# for i in range(ulang):
#     print("data ke - " + str(i+1))
#     nama = input("Masukan NIM Anda: ")
#     uts = int(input("Masukan Nilai UTS: "))
#     uas = int(input("Masukan Nilai UAS: "))
#     print("NiM anda adalah %s nilai uts anda %i nilai uas anda %i" % (nama,uts,uas))
#     print("============================\n")

#latihan Soal While
harga = {
    'D': 2500,  # 'D' adalah key, 2500 adalah value
    'P': 2000,
    'S': 1500
}

nama_potong = {
    'D' or 'd': 'Dada',
    'P' or 'p': 'Paha',
    'S' or 's': 'Sayap'
}

# List ini akan menyimpan detail pesanan pelanggan
pesanan = []
total = 0

print("========================================")
print("    GEROBAK FRIED CHICKEN  ")
print("========================================")
print("Daftar Harga:")
print("  [D] Dada   : Rp. 2500")
print("  [P] Paha   : Rp. 2000")
print("  [S] Sayap  : Rp. 1500")
print("----------------------------------------")

try:
    banyak_jenis = int(input("Banyak Jenis: "))
except ValueError:
    print("Maaf Tolong Input Angka")
    exit()  

for i in range(banyak_jenis):
    print(f"\n--- Pesanan Jenis ke-{i+1} ---")
    
    while True:
        # .upper() mengubah input menjadi huruf besar (jadi 'd' menjadi 'D')
        kode = input("Masukkan Kode Potong [D/P/S]: ").upper()
        if kode in harga:
            break 
        else:
            print("Kode Not valid")

    while True:
        try:
            jumlah_beli = int(input("Masukkan Banyak Beli: "))
            if jumlah_beli > 0:
                break  
            else:
                print("Pembelian Harus 1.")
        except ValueError:
            print("Maaf Tolong Input Angka")
    
    # Ambil harga dan nama dari dictionary kita
    harga_satuan = harga[kode]
    nama_item = nama_potong[kode]
    
    # Hitung subtotal untuk item ini
    subtotal = harga_satuan * jumlah_beli
    
    # Tambahkan subtotal item ini ke total harga keseluruhan
    total += subtotal
    
    # Simpan detail item ini di list 'detail_pesanan' untuk dicetak nanti
    pesanan.append({
        'nama': nama_item,
        'jumlah': jumlah_beli,
        'harga': harga_satuan,
        'subtotal': subtotal
    })


# Hitung pajak (10% dari total)
pajak = total * 0.10  # 0.10 adalah 10%

# Hitung tagihan akhir
total_bayar = total + pajak

print("\n\n========================================")
print("      STRUK PEMBELIAN      ")
print("========================================")
# Header tabel struk
print(f"Jenis Potong, Jml, Harga satuan, Jumlah")
print("----------------------------------------")

# Loop untuk mencetak setiap item yang dibeli
for item in pesanan:
    print(f"{item['nama']}, {item['jumlah']}, Rp.{item['harga']}, Rp.{item['subtotal']}")

print("----------------------------------------")
# Mencetak total, pajak, dan total bayar
print(f"Subtotal: Rp.{total}")
print(f"Pajak (10%): Rp.{pajak}")
print(f"Total Bayar: Rp.{total_bayar}")