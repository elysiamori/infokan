#Latihan
print("Sandi A-N")

#List menu
gg = ["AKU","GG","PAQUITO"]
while True:
    print("Latihan")
    print("1.Login sandi")
    print("2.Tambah sandi")
    print("3.Melihat sandi")
    
    n = int(input("Pilih menu : "))

#Condition
    if n == 1:
        s = str(input("Sandi :"))
        while True:
            if s == gg[0] and gg[1] and gg[2]:
                print("Selamat datang")
                break
                

            else:
                print("Terima Kasih")
                break

                a = int(input("Tekan 1 Untuk Login sandi lagi : "))
                

    elif n == 2:
        while True:
            print("Silahkan tambah kan sandi")
            gg.append(input("Masukan sandi : "))
            print(gg)

            z = int(input("Tekan 1 Untuk menambah kan lagi : "))

            if z == 1:
                continue

            else:
                break

    elif n == 3:
        print(gg)

    else:
        print("Salah Input")
        break

    




    

