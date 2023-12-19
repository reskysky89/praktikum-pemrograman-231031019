a = True  # Inisialisasi variabel a dengan True
jln = 0   # Inisialisasi variabel jln dengan 0

while a:  # Memulai loop while dengan kondisi a
    if jln != 5:  # Jika nilai jln tidak sama dengan 5
        jln += 1  # Tambahkan 1 ke nilai jln (langkah iterasi)
        print(f'Menjalankan program sebanyak {jln} kali')  # Cetak pesan jumlah iterasi
    else:  # Jika nilai jln sama dengan 5
        a = False  # Setel a menjadi False untuk menghentikan loop

# Program keluar dari loop saat nilai a menjadi False
