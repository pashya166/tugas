#tugas E-learing
print(" Gaji Karyawan PT. DINGIN DAMAI ")

nama_karyawan = input("Masukkan Nama Karyawan: ")
golongan = int(input("Masukkan Golongan (1/2/3): "))
pendidikan = input("Masukkan Pendidikan (SMA/D1/D3/S1): ")
jumlah_jam_kerja = int(input("Masukkan Jumlah Jam Kerja: "))
GAJI_POKOK = 300000

# Tunjangan Jabatan
persentase_jabatan = 0
if golongan == 1:
    persentase_jabatan = 0.05
elif golongan == 2:
    persentase_jabatan = 0.10
elif golongan == 3:
    persentase_jabatan = 0.15
else:
    print("Golongan tidak valid!")

tunjangan_jabatan = persentase_jabatan * GAJI_POKOK

# Tunjangan Pendidikan
persentase_pendidikan = 0
if pendidikan == "SMA" or pendidikan == "sma":
    persentase_pendidikan = 0.025
elif pendidikan == "D1" or pendidikan == "d1":
    persentase_pendidikan = 0.05
elif pendidikan == "D3" or pendidikan == "d3":
    persentase_pendidikan = 0.20
elif pendidikan == "S1" or pendidikan == "s1":
    persentase_pendidikan = 0.30
else:
    print("Pendidikan tidak valid!")

tunjangan_pendidikan = int(persentase_pendidikan * GAJI_POKOK)

# Honor
JAM_NORMAL = 8
UPAH_LEMBUR_PER_JAM = 3500
honor_lembur = 0
if jumlah_jam_kerja > JAM_NORMAL:
    jam_lembur = jumlah_jam_kerja - JAM_NORMAL
    honor_lembur = jam_lembur * UPAH_LEMBUR_PER_JAM

#hitung total gaji
total_gaji = int(GAJI_POKOK + tunjangan_jabatan + tunjangan_pendidikan + honor_lembur)

#hasil output
print("==========================================")
print("karyawan yang bernama  :   "+str(nama_karyawan))
print("Tunjangan jabatan      :   "+str(tunjangan_jabatan))
print("Tunjangan Pendidikan   :   "+str(tunjangan_pendidikan))
print("Honor lembur           :   "+str(honor_lembur) )
print("Total gaji             :   "+str(total_gaji))