# Fungsi Rekursif Fibonacci
def fibonacci(n):
    if n < 0:
        print('Tidak ada bilangan yang bernilai negatif')
    elif n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Program Utama
nilai = 20
hasil = fibonacci(nilai)
print('Fibonacci(%d) = %d' % (nilai, hasil))


#input
# Fungsi Rekursif Fibonacci
def fibonacci(n):
    if n < 0:
        print('Tidak ada bilangan yang bernilai negatif')
    elif n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Input dari pengguna
nilai = int(input("Masukkan nilai n untuk deret Fibonacci: "))

# Menampilkan hasil deret Fibonacci hingga n
for i in range(nilai + 1):
    print(f'Fibonacci({i}) = {fibonacci(i)}')
