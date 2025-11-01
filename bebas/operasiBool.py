# operasi logika atau boolean

# or , and , not , xor

#Not
print('=====Not=====')
a = True
c = not a

print('data a =', a)
print('------------Not')
print('data c =', c)

#OR jika salah satu true maka dia akan true
print('=====OR=====')
a = False
b = False
c = a or b
print(a,'OR',b,'=',c)

a = True
b = False
c = a or b
print(a,'OR',b,'=',c)

a = False
b = True
c = a or b
print(a,'OR',b,'=',c)

a = True
b = True
c = a or b
print(a,'OR',b,'=',c)

#AND jika nilai 2 buah true maka akan true
print('=====AND=====')
a = False
b = False
c = a and b
print(a,'AND',b,'=',c)

a = True
b = False
c = a and b
print(a,'AND',b,'=',c)

a = False
b = True
c = a and b
print(a,'AND',b,'=',c)

a = True
b = True
c = a and b
print(a,'AND',b,'=',c)

#XOR hanya true jika salah satu true sisanya false
print('=====XOR=====')
a = False
b = False
c = a ^ b
print(a,'XOR',b,'=',c)

a = True
b = False
c = a ^ b
print(a,'XOR',b,'=',c)

a = False
b = True
c = a ^ b
print(a,'XOR',b,'=',c)

a = True
b = True
c = a ^ b
print(a,'XOR',b,'=',c)

