#minggu 1
print("=======================")
print("Dhisa Luthfi Zibrani")
print("Saya adalah Mahasiswa Baru UBSI")
print("Fakultas Teknik & Informatika")
print("Jurusan Informatika")
print("=======================")


#minggu 2
nilai = 8
if nilai <= 5:
    print("Nilai jelek")
    print("Tidak Lulus")
else:
    print("Nilai bagus")
    print("Lulus")

#Latihan Pertemuan 2
hrg = 15000 
print(f"Harga:Rp {hrg}" )
brt = int(input("masukan brt(kg): "))


byr = hrg * brt
print(f"Rp{byr}")


kata = 'Kuliah'
kalimat = "BSI aja!"
paragrph = """Kuliah.....
BSI aja!"""

print(kata)
print(kalimat)
print(paragrph)

#minggu 1
#komentar Pertama, Komentar tidak akan di anggap baris kode oleh program
print("Universita Bina Sarana Informatikka") #komentar kedua

#minggu 2
var1= 'Hello Python!'
var2= var1[:6]
print(var1)
print("Strinng Update: - ", var1[:6] + 'world')

#minggu 1
"""contoh penggunaan komentar 
dalam bentuk paragraf"""
print("Universitas Bina Sarana Informatika")

'''contoh penggunaan komentar 
dalam bentuk paragraf'''

#minggu 2
str1= 'Hello'
str2= 'Python'

#menggunakan +
print('str1 + str2 =', str1 + str2)

# menggunakan -
print('str1 * 3 =', str1 * 3)

nim = input("masukan nim anda:")
angka = input("masukan angka:")

print(nim)
print(angka)

print("=+=+=+ Data Mahasiswa =+=+=+")
nim = input("NIM: ")
nama = input("Nama: ")
jurusan = input("jurusan: ")
alamat = input("Alamat: ")

print("Hasil cetak data diatas adalah")
print("NIM: " +str(nim))
print("Nama: " +str(nama))
print("JUrusan: " +str(jurusan))
print("Alamat: " +str(alamat))
