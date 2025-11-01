jenis_ps = input("Jenis Ps: ")
jenis_sewa = input("Jenis Sewa: ")
durasi = int(input("Durasi: "))
jt = int(input("Jumlah Transaksi: "))

harga = None
bonus = False

if jenis_sewa == "hari":
    durasi_jam = durasi * 24
else:
    durasi_jam = durasi

if jt > 5:
    durasi_jam = max(0, durasi_jam - 2)
    bonus = True

if jenis_ps == 'ps3':
    if jenis_sewa == 'hari':
        durasi = durasi * 24
        if durasi > 72:
            harga = (400000/24*durasi)*0.85
        else:
            harga = 400000/24*durasi
    else:
        if durasi > 3:
            harga = (20000*durasi)*0.95
        else:
            harga = 20000 * durasi

elif jenis_ps == 'ps4':
    if jenis_sewa == 'hari':
        durasi = durasi * 24
        if durasi > 72:
            harga = (500000/24*durasi)*0.85
        else:
            harga = 500000/24*durasi
    else:
        if durasi > 3:
            harga = (25000*durasi)*0.95
        else:
            harga = 25000 * durasi

elif jenis_ps == 'ps5':
    if jenis_sewa == 'hari':
        durasi = durasi * 24
        if durasi > 72:
            harga = (600000/24*durasi)*0.85
        else:
            harga = 600000/24*durasi
    else:
        if durasi > 3:
            harga = (30000*durasi)*0.95
        else:
            harga = 30000 * durasi

else:
    print("Seriusan Lu???")

print(harga)