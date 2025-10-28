# operasi aritmatika

a = 12
b = 5

# operasi +
hasil = a + b 
print(a,'+',b,'=', hasil)

# operasi -
hasil = a - b 
print(a,'-',b,'=', hasil)

# operasi *
hasil = a * b 
print(a,'*',b,'=', hasil)

# operasi /
hasil = a / b 
print(a,'/',b,'=', hasil)

# operasi  eksponen / pangkat (**)
hasil = a** b 
print(a,'**',b,'=', hasil)

# operasi  modulus %
hasil = a % b 
print(a,'%',b,'=', hasil)

# operasi  floo divison //
hasil = a // b 
print(a,'//',b,'=', hasil)

# prioritas operasi, operasional precedence
'''
        1.()
        2.exponen **
        3.perkalian * / ** % //
        4.plus dan minus + -
'''
x = 3
y = 2
z = 4

hasil = x ** y * z + x / y - y % z // x 
print(x,'**',y,'*',z,'+',x,'/',y,'-',y,'%',z,'//', x, '=', hasil)

hasil = x + y * z
print(x,'+',y,'*',z,'=', hasil)
# kurang ambil langkah pertama
hasil = (x + y) * z
print('(',x,'+',y,')*',z,'=',hasil)