# fungsi f string untuk estetik(rapi) / memperindah / mempermudah pembacaan

a = 5
b = 3
c = a + b 
print("data:", c ,"bertipe; ",type (c))

print(f"data: {c} bertipe: " , type(c))

# Kode untuk warna merah: \033[91m
# Kode untuk reset: \033[0m

print("\033[92m\033[1m\033[3mIni adalah tulisan berwarna merah.\033[0m")
print("Ini adalah tulisan normal lagi.")