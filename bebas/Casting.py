#Casting
"""Casting adalah merubah suatu tipe data ke tipe yang lain"""
#Tipe data:: String, Int, Float, Bool

#Integer
print(">>Integer<<")
data_int = 18
print("Data awal = ", data_int , "Bertipe : ", type(data_int))

data_flot = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int) #akan false jika nilai int = 0
print("Data = ", data_flot , "Bertipe : ", type(data_flot))
print("Data = ", data_str , "Bertipe : ", type(data_str))
print("Data = ", data_bool , "Bertipe : ", type(data_bool))
print("=============================================")

#Float
print(">>Float<<")
data_flot = 2.3
print("Data awal = ", data_flot , "Bertipe : ", type(data_flot))

data_int = int(data_flot)
data_str = str(data_flot)
data_bool = bool(data_flot) 
print("Data = ", data_int , "Bertipe : ", type(data_int))
print("Data = ", data_str , "Bertipe : ", type(data_str))
print("Data = ", data_bool , "Bertipe : ", type(data_bool))
print("=============================================")

#String
print(">>String<<")
data_str = "18"
print("Data awal = ", data_str , "Bertipe : ", type(data_str))

data_int = int(data_str)
data_flot = float(data_str)
data_bool = bool(data_str)
print("Data = ", data_int , "Bertipe : ", type(data_int))
print("Data = ", data_flot , "Bertipe : ", type(data_flot))
print("Data = ", data_bool , "Bertipe : ", type(data_bool))
print("=============================================")

#Boolean
print(">>Boolean<<")
data_bool = False # jika (True)= int/float = 1 , jika (False) = int/float = 0
print("Data awal = ", data_bool , "Bertipe : ", type(data_bool))

data_int = int(data_bool)
data_flot = float(data_bool)
data_str = str(data_bool)
print("Data = ", data_int , "Bertipe : ", type(data_int))
print("Data = ", data_flot , "Bertipe : ", type(data_flot))
print("Data = ", data_str , "Bertipe : ", type(data_str))
print("=============================================")