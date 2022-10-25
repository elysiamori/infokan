#Periode Sebuah 
while True:
    print("Menghitung Periode Kepimpinan")
    t = int(input("Dari Tahun Berapa Awalnya :"))
    print("1 Periode = 4 tahun")
    n = int(input("Berapa periode yang diinginkan : "))

#Algorithm
    p = (n * 4) + t

#Output
    print("Tahun Selesainya kepemimpinan : ", p )
    y = int(input("Tekan 1 Untuk Melanjutkan : "))

    if y == 1:
        continue

    else:
        print("Terima Kasih")
        break
 



