print("Input Nama")
print("1.Fahrenheit")
print("2.Kelvin")
print("3.Reamur")
celsius = (input("Pilih konversi :"))

c = int(input ("Celcius : "))
f = 9/5 * c + 32
k = c + 273
r = 4/5 * c

if  celsius == "1":
    print("Konversi Fahrenheit", f)

elif celsius == "2":
    print("Konversi Kelvin", k)

elif celsius == " 3":
    print("Konversi Reamur", r)

else:
    print("Pilihan salah")






