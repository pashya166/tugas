# Input data
"""input di fungsikan untuk memperoleh/meminta data oleh user"""
# input data pasti bertipe "str"

# Data = input("masukan data: ")
# print(f"data: {Data}, bertype: ",type(Data))

"""jika ingin mengubah type datanya kita harus menulis 
tipe data yang kita mau di code nya:"""
#integer = int(input())
#Float = float(input())
#boolean = bool(input())

#untuk mengambil data (false) di boolean harus di ubah dulu ke integer
Data = bool(int(input("masukan data: ")))
print(f"data: {Data}, bertype: ",type(Data))
