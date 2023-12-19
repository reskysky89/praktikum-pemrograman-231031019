# Fungsi Rekursif factorial dengan perulangan
def faktorial(nilai):
    if nilai <= 1:
        return 1
    else:
        return nilai * faktorial(nilai - 1)

# Program Utama
for i in range(11):
    print('%2d ! = %d' % (i, faktorial(i)))
# Fungsi Rekursif factorial dengan perulangan
def faktorial(nilai):
    if nilai <= 1:
        return 1
    else:
        return nilai * faktorial(nilai - 1)

# Input dari pengguna
nilai = int(input("Masukkan nilai untuk menghitung faktorial: "))

# Menampilkan hasil faktorial hingga nilai yang dimasukkan
for i in range(nilai + 1):
    print('%2d ! = %d' % (i, faktorial(i)))

