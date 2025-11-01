#operasi komparasi

#setiap hasil dari operasi komparasi adalah boolean

# >,<,>=,<=,==,!=,is,is not

a = 5
b = 2

# lebih besar dari >
print('============ Lebih besar dari (>)')
hasil = a > 3
print(a,'>',3,'=',hasil)
hasil = b > 3
print(b,'>',3,'=',hasil)
hasil = b > 2
print(b,'>',2,'=',hasil)

# kurang dari <
print('============ Kurang dari (>)')
hasil = a < 3
print(a,'<',3,'=',hasil)
hasil = b < 3
print(b,'<',3,'=',hasil)
hasil = b < 2
print(b,'<',2,'=',hasil)

# lebih dari sama dengan >=
print('============ Lebih dari sama dengan (>=)')
hasil = a >= 3
print(a,'>=',3,'=',hasil)
hasil = b >= 3
print(b,'>=',3,'=',hasil)
hasil = b >= 2
print(b,'>=',2,'=',hasil)

# kurang dari sama dengan <=
print('============ Kurang dari sama dengan (>=)')
hasil = a <= 3
print(a,'<=',3,'=',hasil)
hasil = b <= 3
print(b,'<=',3,'=',hasil)
hasil = b <= 2
print(b,'<=',2,'=',hasil)

# sama dengan ==
print('============ sama dengan (==)')
hasil = a == 3
print(a,'==',3,'=',hasil)
hasil = b == 3
print(b,'==',3,'=',hasil)
hasil = b == 2
print(b,'==',2,'=',hasil)

# tidak sama dengan !=
print('============ tidak sama dengan (!=)')
hasil = a != 3
print(a,'!=',3,'=',hasil)
hasil = b != 3
print(b,'!=',3,'=',hasil)
hasil = b != 2
print(b,'!=',2,'=',hasil)

# 'is' sebagai komparasi objek identity
x = 5 
y = 5
print('nilai x =', x, 'id = ',hex(id(x))) 
print('nilai y =', y, 'id = ',hex(id(y))) 
hasil = x == 5
print('x is y =', hasil)

# 'is not' sebagai komparasi objek identity
x = 5 
y = 6
print('nilai x =', x, 'id = ',hex(id(x))) 
print('nilai y =', y, 'id = ',hex(id(y))) 
hasil = x != 6
print('x is not y =', hasil)