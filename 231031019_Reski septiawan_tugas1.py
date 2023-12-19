# Meminta input bilangan X dari pengguna
X = int(input("Masukkan bilangan X: "))

# Cek apakah X adalah bilangan ganjil atau bukan
if X % 2 == 1:
    print(f"{X} adalah bilangan Ganjil")
else:
    print(f"{X} adalah bilangan Bukan Ganjil")
