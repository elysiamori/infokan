n = int(input("Jam masuk : "))
m = int(input("Jam Keluar : "))
if m > n:
    jam_kerja = m - n
else:
    jam_kerja = (12 + m) - n

print("Lama bekerja "+str(jam_kerja)+ "Jam")
