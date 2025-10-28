toko ="Toko mainan anak"
bintang ="*********************"

jarak = 50
print(toko.center(jarak))
print(bintang.center(jarak))

nama = str(input("Masukan Nama Pembei: "))
kode = str(input("Masukan Kode Mainan: "))
harga= int(input("Masukan Harga: "))
jumlah_beli= int(input("Masukan Jumlah Beli: "))
total = harga * jumlah_beli
print("===============================")

lebar_label = 15 
print(f"{'Nama Pembeli':<{lebar_label}} = {nama}")
print(f"{'Kode Kue':<{lebar_label}} = {kode}")
print(f"{'Harga':<{lebar_label}} = {harga}")
print(f"{'Jumlah Beli':<{lebar_label}} = {jumlah_beli}")
print(f"{'Total':<{lebar_label}} = {total}")


