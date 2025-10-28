print(">>>operator penugasan<<<")
print(">>>operator penugasan<<<")
x = 5
x += 3
x -= 2
x *= 2
x /= 4
print(x)

print(">>>operator logika<<<")
a = True
b = False
print(a and b)
print(b or a)
print(not b)

print(">>>operator bitwise<<<")
# Bitwise AND (&)
a = 10
b = 4  
hasil_and = a & b
print(f"Hasil dari a & b adalah: {hasil_and}")

# Bitwise OR (|)
a = 10
b = 4
a | b
hasil_or = a | b
print(f"Hasil dari a | b adalah: {hasil_or}")

# Operator ^ (XOR)
a = 10
b = 4
c = a ^ b
print(f"Hasil a ^ b adalah: {c}")

# Operator ~ (NOT)
a = 10 
c = ~a
print(f"Hasil ~a adalah: {c}")

# Operator << (Left Shift)
a = 10  
c = a << 2
print(f"Hasil a << 2 adalah: {c}")

# Operator >> (Right Shift)
a = 10 
c = a >> 2
print(f"Hasil a >> 2 adalah: {c}")

print(">>>operator identitas<<<")
#  Nilai Sama, Objeknya Sama (is)
x = 10
y = 10
print(x is y)

# Nilai Sama, Objeknya Beda (is)
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(list1 is list2)

# Memeriksa dengan (is not)
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(list1 is not list2)

print(">>>operator keanggotaan<<<")
# in: Ngecek apakah suatu nilai ada di dalam urutan
kalimat = "Hello, dunia coding!"

print("coding" in kalimat)
print("python" in kalimat)

# not in: Kebalikannya, ngecek apakah suatu nilai tidak ada di dalam urutan
print("coding" not in kalimat)
print("python" not in kalimat)