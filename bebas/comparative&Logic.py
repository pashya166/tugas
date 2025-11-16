# latihan logika dan komparasi

# membuat gabungan area rentang dari angka
# +++++++3----------10+++++++++

inputUser = float(input("Masukan angka bernilai\nkurang dari 3\natau \nlebih dari 10\n:"))

# ++++++3---------------
# Memeriksa angka kurang dari 3
isKurangdari = (inputUser < 3)
print("Kurang dari 3", isKurangdari)

# -------------------10++++++++
# memeriksa angka lebih dari 10
isLebihdari = (inputUser > 10)
print("Lebih dari 10", isLebihdari)


# +++++++3----------10+++++++++
isCorrect = isKurangdari or isLebihdari
print("angka yang ada anda masukan:", isCorrect)


# ------3+++++++10--------
# kasus irisan
print("\n",10*"=","\n")
inputUser = float(input("Masukan angka bernilai\nlebih dari 3\ndan \nkurang dari 10\n:"))

# ------3+++++++++++++
# lebih dari 3
isLebihdari = inputUser > 3
print("Lebih dari 3 =", isLebihdari)

# +++++++++++++++++++10------
# kurang dari 10
isKurangdari = inputUser < 10
print("Kurang dari 10 =", isKurangdari)

# ------3+++++++10--------
isCorrect = isKurangdari or isLebihdari
print("angka yang ada anda masukan:", isCorrect)