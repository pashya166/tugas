#latihan 1
ver1 = "Hello Python"
ver2 = "Programing With Python"

print(ver1)
print(ver2)

#latihan 2
var1 = "Hello Python"
var2 = "I Love Python"
print("var1[0]", var1[0])
print("var2[2:6]:", var2[2:6])

#latihan 3
var1= 'Hello Python!'
var2= var1[:6]
print(var1)
print("Strinng Update: - ", var1[:6] + 'world')

#latihan 4
str1= 'Hello'
str2= 'Python'

#menggunakan +
print('str1 + str2 =', str1 + str2)

# menggunakan -
print('str1 * 3 =', str1 * 3)

#latihan 5
string = 'I love Python'
print(len(string))

#latihan 6
#print("He said, "What's There?")

#latihan 7
# menggunkan kutip tiga
print('''He said, "Whats's there"''')

# menggunkan karakter escpape untuk tanda kutip tunggal
print('He said, "Whats\'s there"')

# menggunkan karakter escape untuk tanda kutip ganda
print("He said, \"Whats's there\"")

#latihan 8
print("Ini adalah garis pertama\nDan ini baris dua")
print("Ini adalah \x48\x45\x58")

#latihan 9
print("This is \x61 \ngood example")
print(r"This is \x61 \good example")

#latihan 10
# menggunakan posisi default
default_order = "{} , {} dan {}".format("Budi", "Galih", "Ratna")
print('\n--- Urutan default ---')
print(default_order)

# menggunakan argument posisi
positional_order = "{1}, {0} dan {2}".format("Budi", "Galih", "Ratna")
print('\n--- Urutan berdasarkan posisi ---')
print(positional_order)

#latihan 11
# format integer
print("{0} bila diubah jadi biner menjadi {0:b}".format(12))

# format float
print("Format eksponensial: {0:e}".format(1566.345))

# pembulatan
print("Sepertiga sama dengan: {0:.3f}".format(1/3))

# Meratakan string
print('|{:<10}|{:^10}|{:>10}|'.format('beras', 'gula', 'garam'))

#latihan 12
x = 12.3456789
print("Nilai x = %.2f" % x)
print("Nilai x = %.4f" % x)

#latihan 13
print("Universitas Bina Sarana Informatika".lower())
print("Universitas Bina Sarana Informatika".upper())
print("I love programming in Python".split())
print("I love Python".startswith("I"))
print("Saya belajar Python".endswith("on"))
print(' - '.join(['I', 'love', 'you']))
print("Belajar Java di BSI".replace('Java', 'Python'))

#latihan 14
print(int(2.5))
print(int(3.8))
print(float(5))

#latihan 15
print((1.1 + 2.2) == 3.3)
print(1.1 + 2.2)

#latihan 16
import decimal
#output: 0.1
print(0.1)
#output: Decimal('0.1000000000000000055511151231257827021181583404541015625')
print(decimal.Decimal(0.1))

#latihan 17
import fractions
#output: 3/2
print(fractions.Fraction(1.5))
#output: 1/3
print(fractions.Fraction(1,3))

#latihan 18
from fractions import Fraction as F
# Output: 2/3
print(F(1,3) + F(1,3))
# Output: 6/5
print(1 / F(5,6))
# Output True
print(F(-3,10) < 0)

#latihan 19
import math
# Output: 3.141592653589793
print(math.pi)
# Output: -1.0
print(math.cos(math.pi))
# Output: 148.4131591025766
print(math.exp(5))
# Output: 2.0
print(math.log10(100))
# Output: 120
print(math.factorial(5))

#latihan 20
nilai1 = 10
nilai2 = 8
penjumlahan = nilai1 + nilai2
print(nilai1, "+", nilai2, "=", penjumlahan)
pengurangan = nilai1 - nilai2
print(nilai1, "-", nilai2, "=", pengurangan)
perkalian = nilai1 * nilai2
print(nilai1, "x", nilai2, "=", perkalian)
pembagian = nilai1 / nilai2
print(nilai1, "/", nilai2, "=", pembagian)
pemangkatan = nilai1 ** nilai2
print(nilai1, "**", nilai2, "=", pemangkatan)
pembagian_bulat = nilai1 // nilai2
print(nilai1, "//", nilai2, "=", pembagian_bulat)

#latihan 21
nama = input("Masukkan nama Anda : ")
print("Hai " + nama + " Selamat Bergabung di UKM Mapasika")

#latihan 22
nilai1 = int(input("Masukkan Nilai Pertama : "))
nilai2 = int(input("Masukkan Nilai Kedua : "))
penjumlahan = nilai1 + nilai2
print(nilai1, "+", nilai2, "=", penjumlahan)
pengurangan = nilai1 - nilai2
print(nilai1, "-", nilai2, "=", pengurangan)
perkalian = nilai1 * nilai2
print(nilai1, "x", nilai2, "=", perkalian)
pembagian = nilai1 / nilai2
print(nilai1, "/", nilai2, "=", pembagian)
pemangkatan = nilai1 ** nilai2
print(nilai1, "**", nilai2, "=", pemangkatan)
pembagian_bulat = nilai1 // nilai2
print(nilai1, "//", nilai2, "=", pembagian_bulat)

#latihan 23
nilai1 = int(input("Masukkan Nilai Pertama : "))
nilai2 = int(input("Masukkan Nilai Kedua : "))
operator_lebih_besar = nilai1 > nilai2
print(nilai1, ">", nilai2, "adalah", operator_lebih_besar)
operator_lebih_kecil = nilai1 < nilai2
print(nilai1, "<", nilai2, "adalah", operator_lebih_kecil)
operator_sama_dengan = nilai1 == nilai2
print(nilai1, "==", nilai2, "adalah", operator_sama_dengan)
operator_tidak_sama_dengan = nilai1 != nilai2
print(nilai1, "!=", nilai2, "adalah", operator_tidak_sama_dengan)