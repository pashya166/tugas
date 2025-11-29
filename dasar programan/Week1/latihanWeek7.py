def sapa(nama):
    """Fungsi ini untuk menyapa seseorang sesuai nama yang dimasukan sebagai parameter"""
    print("Hi, " + nama + ". Apa Kabar?")

# pemanggil fungsi
# output: Hi, Umar. Apa Kabar?
sapa('Umar')

# definsi fungsi print_string
def print_string( str ):
    """menampilkan argumen string str ke layar"""
    print(str)

# kita memanggil fungsi dengan kata kunci
print_string( str = "Hello Python")

# Definisi Fungsi
def print_info(nama, usia):
    """Fungsi ini menampilkan info yang dimasukan"""
    print("Nama: ", nama)
    print("Usia: ", usia)

# memanggil fungsi
# output
# nama: budi
# usia: 25
print_info( usia = 25, nama = "Budi")

# Definisi Fungsi 
def print_info( nama, usia= 17):
    print("Nama: ", nama)
    print("Usia: ", usia)

print_info( usia = 29, nama = "Galih")

print_info(nama= 'Galih')

# Definisi Fungsi
def print_info( arg1, *vartuple):
    """Fungsi untuk mampilkan nilai argumen sembarang yang dilewatkan"""
    print ("Outputnya adalah: ")
    print(arg1)
    for var in vartuple:
        print(var)

# pemanggil fungsi
# satu argumen
print_info( 10 )

# empat argumen
print_info(10, 30, 50, 70)

# Variabel global
# definisi fungsi
total = 0
def sum(arg1, arg2):
    """Menambahkan variabel dan mengembalikan hasilnya"""
    total = arg1 + arg2;
    # total adalah variabel lokal di fungsi ini
    print("Dalam fungsi nilai total : ", total)
    return total

# pemanggil fungsi sum
sum (10, 20)
print("Di luar fungsi nilai total : ", total)