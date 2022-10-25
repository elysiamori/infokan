#Keterangan
from os import system
system("cls")
while True:
    print("Kalkulator")
    print("1.Tambah")
    print("2.Kurang")
    print("3.Kali")
    print("4.Bagi") 
    print("5.Hasil Bagi")

#Deklarasi
    j = int(input("Pilih opsi : "))
    p = float(input("Angka 1 : "))
    q = float(input("Angka 2 : "))

#Algoritma
    t = p + q
    k = p - q
    x = p * q
    b = p / q
    v = p % q

#Function
    if j == 1:
        print("Hasilnya : ",t)

    elif j == 2:
        print("Hasilnya : ",k)

    elif j == 3:
        print("Hasilnya : ",x)

    elif j == 4:
        print("Hasilnya : ",b)

    elif j == 5:
        print("Hasilnya : ",v)

    else:
        print("Salah input")

    s = int(input("Tekan 1 Untuk Memakai lagi : "))

    if s == 1:
        continue

    else:
        print("Thank you")
        break
