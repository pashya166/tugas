#minggu 6
my_list = ["I","Love","Pyhton","Programming","2017"]

#output 1
my_list[0]

#output:python
my_list[2]

#list dalam list
your_list = ["hello",[1,2,3],"Python"]

#output 1
print(your_list[1][0])

#output3
print(your_list[1][2])

#indexeror
#my_list[6]
my_list = ['p','y','t','h','o','n']

#output:n
print(my_list[-1])

#output:h
print(my_list[-3])

my_list = ['p','y','t','h','o','n','i','n','d','o']

#anggota list dari 3 s/d (dari h s/d n)
print(my_list[3:6])

print(my_list[4:1])

#anggota list dari 0 s/d 4
print(my_list[:5])

#index dari belakang dari -1 s/d -4
print(my_list[-1:-5])

#misal ada yang salah
ganjil = [1,3,4,7,9]

#ubah item ke 3 (index ke 2)
ganjil[2]=5
print(ganjil)

#mengubah sekali banyak
ganjil[2:5]= [11,13,15]
print(ganjil)

ganjil = [1,3,5,7]
ganjil.append(9)
print(ganjil)
ganjil.extend([11,13,15])
print(ganjil)

genap = [2,4,6]
print(genap + [8,10,12])
print(['p','y']*2)

ganjil = [5,7,11,13,15]
#kita akan menyisipkan 9 setelah angka 7

ganjil.insert(2,9)
print(ganjil)

my_list = ['p','y','t','h','o','n','i','n','d','o']
my_list.remove('p')
#output P bakal ilang
print(my_list)

my_list.remove('n')
#remove hanya menghilangkan angka yang diinginkan

#output 'y'
print(my_list.pop(1))

del my_list[2]
print(my_list)

my_list.clear()
#output []
print(my_list)

alfabet = ['a','b','d','f','e','c','h','g','j','i']
alfabet.sort()
print(alfabet)
alfabet.sort(reverse=True)
print(alfabet)

alfabet = ['a','c','d','e','b']
alfabet.reverse()
print(alfabet)

#membuat turple kosong
my_turple = ()
print(my_turple)

#turple dengan 1 elemen
#output: (1,)
my_turple = (1,)
print(my_turple)

#turple berisi integer
#output: (1,)
my_turple = (1,2,3)
print(my_turple)

#turple bersarang
#output ("hello", [1,2,3],(4,5,6))
my_turple = ("hello", [1,2,3],(4,5,6))
print(my_turple)

#tuple bisa tidak memakai ()
#output (1,2,3)
my_turple = 1,2,3

#memasukan anggota turple ke variabel yang bersesuaian
#a berisi 1, b berisi 2, c berisi 3
#output 1,2,3
a,b,c = my_turple
print(a,b,c)

my_turple = ['p','r','o','g','r','a','m','m','i','n','g']
#akses dari index 0 s/d 2

#output: (p,r,o)
print(my_turple[:3])

#akses dari index 2 s/d 5
#output: (r,o,g,r)
print(my_turple[2:6])

#akses dari index 3 sampai akhir 
#output: (p ilang)
print(my_turple[3:])

my_turple = (2,3,4,[5,6])
#kita tidak bisa mengubah anggota turple

#my_turple = 8

#tapi list didalam turple bisa diubah
#output (2,3,4,[7,6])
my_turple = ('p','y','t','h','o','n')
print(my_turple)



#del my_turple[0]

del my_turple
my_turple  = (1,2,3,'a','b','c')

#menggunakan in
#output false
print('3' in my_turple)

#output false
print('e' in my_turple)

#menggunakan not in
#output True
print('k' not in my_turple)

#output 
#Hi Galih
#Hi Ratna

nama = ('Galih', 'Ratna')
for name in  nama:
    print('Hi', name)

my_turple = ('p','y','t','h','o','n')
#count
#output: 2
print(my_turple.count('n'))

#index
#output: 4
print(my_turple.index('n'))