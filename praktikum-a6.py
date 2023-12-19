# Inisialisasi variabel a dengan nilai True
a = True

# Memulai loop while dengan kondisi a
while a:
    # Meminta input dari pengguna dan menyimpannya dalam variabel pilih
    pilih = input("Pilihan: ")
    
    # Memeriksa apakah input pengguna adalah 'ya'
    if pilih == 'ya':
        print('Selamat Datang')
        break  # Keluar dari loop karena kondisi telah terpenuhi
    
    # Memeriksa apakah input pengguna adalah 'tidak'
    elif pilih == 'tidak':
        print('Sampai Jumpa')
        break  # Keluar dari loop karena kondisi telah terpenuhi
    
    # Blok ini akan dieksekusi jika input pengguna tidak 'ya' atau 'tidak'
    else:
        print('Anda mungkin typo! (ya/tidak)')

# Program akan keluar dari loop saat kondisi a tidak lagi terpenuhi
