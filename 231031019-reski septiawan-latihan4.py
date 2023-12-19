# Menerima input pendapatan dari pengguna
pendapatan = int(input("Pendapatan: "))

# Inisialisasi variabel bonus, persentase, dan jumlah total
bonus = 0
persentase = 0

# Menghitung bonus dan persentase berdasarkan pendapatan
if pendapatan <= 1000:
    persentase = 0
elif pendapatan <= 2000:
    persentase = 10
elif pendapatan <= 3000:
    persentase = 20
elif pendapatan <= 4000:
    persentase = 30
elif pendapatan <= 5000:
    persentase = 40
else:
    persentase = 50

bonus = (pendapatan * persentase) / 100
total = pendapatan + bonus

# Cetak hasil
print("Besar Pendapatan:", pendapatan)
print("Besar Persentase:", str(persentase) + "%")
print("Bonus yang didapatkan:", bonus)
print("Jumlah Total:", total)
