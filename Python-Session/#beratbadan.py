#Berat Badan Ideal
while True:
    print("Berat badan")
    print("Jenis Kelamin")
    print("1.Pria")
    print("2.Wanita")
    g = input("Pilihan :")

#Deklarasi
    tb = int(input("Berapa tinggimu :"))

#Algorithm
    p = (tb - 100) - (tb - 100) * 10/100
    w = (tb - 100) - (tb - 100) * 15/100

#Function
    if g == "1":
        print("Berat badan ideal : " + str(p) + " kg")

    elif g == "2":
        print("Berat badan ideal : " + str(w) + " kg" )

    else:
        print("Pilihan salah")

    n = int(input("Tekan 1 Untuk Mengulang :"))

    if n == 1:
        continue
    else:
        print("Thank You")
        break