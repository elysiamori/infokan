n = int(input("Masukan banyak data : "))
v = 1;amo = 0
while v <= n:
    x = float(input("Nilai data ke- " + str(v) + ":"))
    if x < 0:
        print("Not Negative Dude")
    else:
        amo = amo + x
        v = v + 1
ave = amo / n
print("Rata ratanya : ",ave)
print("Jumlahnya : ",amo)
