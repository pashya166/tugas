#latihan 1
#Bila bilangan positif , tampilkan pesan

angka = 5

if angka > 0:
    print(angka, "adalah bilangan positif")

angka = -1
# yang berikut akan bernilai False sehingga tidak dieksekusi
if angka > 0:
    print(angka, "adalah bilangan positif")

#latihan 2
# program menguji apakah sebuah bilangan positif atau negatif
# dan menampilkan pesan ke monitor

bilangan = 8

# coba juga mengubah bilangan menjadi bilangan = -1
# dan perhatikan hasilnya

if bilangan >= 0:
    print("Positif atau 0")
else:
    print("Bilangan negatif")

#latihan 3
'''Disini kita menguji apakah sebuah bilangan adalah bilangan positif, nol, atau negatif
dan menampilkan hasilny ke layar'''

bilangan = 5.5

'''Coba juga mengganti bilangan menjadi
bilangan = 0
bilangan = -5.5 '''

if bilangan > 0:
    print("Bilangan Positif")
elif bilangan == 0:
    print("Nol")
else:
    print("Bilangan negatif")

#latihan 4
kode_baju = input("Masukan Kode Baju [SP/AD] : ")
Ukuran = input("Masukan Ukuran Baju [S/M] : ")

if kode_baju == "SP" or kode_baju == "sp":
    merk = "SuperDry"
    if Ukuran == "S" or Ukuran == "s":
        harga = 45000
    elif Ukuran == "M" or Ukuran == "m":
        harga = 50000
    else:
        harga = 0
elif kode_baju == "AD" or kode_baju == "ad":
    merk = "Adidas"
    if Ukuran == "S" or Ukuran == "s":
        harga = 65000
    elif Ukuran == "M" or Ukuran == "m":
        harga = 70000
    else:
        harga = 0
else:
    merk = "Anda Salah Input Kode Merek"
    harga = 0

print("--------------------------------")
print("Merk baju : " + str(merk))
print("Harga baju : Rp.", harga)

#latihan 5
#Input
pembeli=input("Nama Pembeli : ")
no_hp=input("No. Handphone : ")
jurusan=input("Jurusan [SBY/BL/LMP] : ")

#Proses
if jurusan.upper() =="SBY":
    namajurusan="Surabaya"
    harga=300000
elif jurusan .upper()=="BL":
    namajurusan="Bali"
    harga=350000
else:
    namajurusan="Lampung"
    harga=500000

#Input Jumlah Beli
jumlah=int(input("Masukkan Jumlah Beli : "))

#Proses potongan
if jumlah>=3:
    potongan=(jumlah*harga)*0.1
else:
    potongan=0

total=(jumlah*harga)-potongan

#Cetak Hasil
print("------------------------------------")
print("          PENJUALAN TIKET BUS")
print("                  XYZ")
print("------------------------------------")
print("Nama Pembeli       :"+str(pembeli))
print("No. Handphone      :"+str(no_hp))
print("Kode Jurusan yang dipilih :"+str(jurusan))
print("Nama Kota Tujuan   :"+str(namajurusan))
print("Harga              :"+str(harga))
print("Jumlah Beli        :"+str(jumlah))
print("------------------------------------")
print("potongan yang didapat :"+str(potongan))
print("Total Bayar        :"+str(total))
ubay=int(input("Masukkan Uang Bayar : "))
uangkembali=ubay-total
print("Uang Kembali       :"+str(uangkembali))

#latihan 6
#Menentukan angka genap/ganjil
angka = int(input("Masukan angka: "))

if angka % 2 == 0:
    print(f"{angka} Adalah angka Genap")
else:
    print(f"{angka} Adalah angka ganjil")

#studi kasus pendaftaran mahasiswa baru
print("-----------------------------")
print(" PENDAFTARAN MAHASISWA BARU")
print("-----------------------------")
nama = input("Masukan Nama : ")
nim = int(input("Masukan NIM : "))
jurusan = input("Masukan Jurusan : ")
print("\n-----------------------------")

if jurusan.upper() == "SI":
    namajurusan= "Sistem Informasi"
    kode = "SI"
    harga = 2400000
elif jurusan.upper() == "SIA":
    namajurusan = "Sistem Informasi Akutansi"
    kode = "SIA"
    harga = 2000000
elif jurusan.upper() == "TI":
    namajurusan = "Teknologi Informasi"
    kode = "TI"
    harga = 3000000
else:
    namajurusan = "Jurusan Tidak Ditemukan"
    kode = "Kode Tidak Ditemukan"
    harga = "Eror"

print("Nama Mahasiswa: "+str (nama))
print("NIM: "+str (nim))
print("Kode Jurusan: "+str (jurusan))
print("Nama Jurusan: "+str (namajurusan))
print("Harga per Semester: "+str (harga))

# PROGRAM HITUNG GAJI KARYAWAN
print("=== PROGRAM HITUNG GAJI KARYAWAN ===")

# Layar Masukkan
nama = input("Nama Karyawan        : ")
golongan = input("Golongan Jabatan (1/2/3) : ")
pendidikan = input("Pendidikan (SMA/D1/D3/S1) : ")
jam_kerja = int(input("Jumlah jam kerja     : "))

# Gaji Pokok berdasarkan golongan
if golongan == "1":
    gaji_pokok = 3000000
elif golongan == "2":
    gaji_pokok = 3500000
elif golongan == "3":
    gaji_pokok = 4000000
else:
    gaji_pokok = 0

# Tunjangan jabatan (20% dari gaji pokok)
tunjangan_jabatan = 0.2 * gaji_pokok

# Tunjangan pendidikan
if pendidikan.upper() == "SMA":
    tunjangan_pendidikan = 0.05 * gaji_pokok
elif pendidikan.upper() == "D1":
    tunjangan_pendidikan = 0.1 * gaji_pokok
elif pendidikan.upper() == "D3":
    tunjangan_pendidikan = 0.15 * gaji_pokok
elif pendidikan.upper() == "S1":
    tunjangan_pendidikan = 0.2 * gaji_pokok
else:
    tunjangan_pendidikan = 0

# Honor lembur (jika jam kerja > 160)
if jam_kerja > 160:
    honor_lembur = (jam_kerja - 160) * 20000
else:
    honor_lembur = 0

# Total gaji
total_gaji = gaji_pokok + tunjangan_jabatan + tunjangan_pendidikan + honor_lembur

# Output
print("\n=== HASIL PERHITUNGAN GAJI ===")
print(f"Karyawan yang bernama : {nama}")

print("Honor yang diterima 💵")
print(f"  Tunjangan Jabatan     : Rp {tunjangan_jabatan:,.0f}")
print(f"  Tunjangan Pendidikan   : Rp {tunjangan_pendidikan:,.0f}")
print(f"  Honor Lembur           : Rp {honor_lembur:,.0f}")
print("-------------------------------------------")
print(f"Total Gaji              : Rp {total_gaji:,.0f}")