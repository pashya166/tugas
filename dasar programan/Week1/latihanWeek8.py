import penggunaan_modul as aritmatika

print(aritmatika.penjumlahan(10, 90))

from math import pow

pangkat_bilangan = pow(3, 3)
print("hasil dari pengangkatan bilangan adalah : ", pangkat_bilangan)

# angka 3 pertama merupakan angka yang akan dipangkatkan
# angka 3 berikutnya adalah jumlah pemangkatan

from math import factorial

bil = int(input("Masukan sebuah bilangan positif:  "))
faktorial = factorial(bil)
print("Bilangan faktorial dari bil adalah: ", faktorial)

from math import*
pangkat_bilangan = pow(3, 3)
print("hasil dari pengangkatan bilangan adalah : ", pangkat_bilangan)
   
bil = int(input("Masukan sebuah bilangan positif:  "))
faktorial = factorial(bil)
print("Bilangan faktorial dari bil adalah: ", faktorial)

import sys 

lists = ['a', 0, 4]
for each in lists:
    try:
        print("Masukan:", each)
        r = 1 / int(each)
        break
    except:
        print("Upps!", sys.exc_info()[0], " terjadi")
        print("Masukan berikutnya.")
        print()
print("Kebalikan dari.", each, " = ", r)