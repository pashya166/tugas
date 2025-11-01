#latihan perhitungan tempratur

#program konvensi celcius satu sama lain
print("\nProgam Konvensi Tempratur\n")

celcius = float(input("Masukan Input suhu dalam celcius: "))
print("suhu adalah", celcius, "Celcius")

#reamur
reamur = (4/5) * celcius
print("suhu dalam reamur adalah", reamur, "Reamur")

#fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print("suhu dalam fahrenheit adalah", fahrenheit, "Fahrenheit")

#kelvin
kelvin = celcius + 273
print("suhu dalam kelvin adalah", kelvin, "Kelvin")
