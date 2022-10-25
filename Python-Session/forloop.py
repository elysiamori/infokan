#ForLoop

b = int(input("Masukan data : "))

nama = []
umur = []

for i in range(0, b):
    print(f"Data ke-{i}")
    input_nama = input("Nama : ")
    input_umur = int(input("Umur : "))

    nama.append(input_nama)
    umur.append(input_umur)

print(nama)
print(umur)