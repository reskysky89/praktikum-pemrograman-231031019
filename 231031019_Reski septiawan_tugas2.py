print('PROGRAM PENJUMLAHAN WAKTU')
print('-'*30)
# Input waktu awal
waktu_awal = input("Masukkan waktu awal (hh:mm): ")
jam, menit = map(int, waktu_awal.split(':'))

# Input waktu yang akan ditambahkan
tambah_jam = int(input("Masukkan jumlah jam yang akan ditambahkan: "))
tambah_menit = int(input("Masukkan jumlah menit yang akan ditambahkan: "))

# Hitung waktu akhir
jam_akhir = (jam + tambah_jam + (menit + tambah_menit) // 60) % 24
menit_akhir = (menit + tambah_menit) % 60

# Cetak waktu akhir
print(f"Waktu sekarang menunjukkan Pukul {jam_akhir:02d}:{menit_akhir:02d}")

print()
print('PROGRAM SELISIH WAKTU')
print('-'*30)
# Input waktu awal
waktu_awal = input("Masukkan waktu awal (hh:mm): ")
jam, menit = map(int, waktu_awal.split(':'))

# Input waktu yang akan dikurangkan
kurang_jam = int(input("Masukkan jumlah jam yang akan dikurangkan: "))
kurang_menit = int(input("Masukkan jumlah menit yang akan dikurangkan: "))

# Hitung waktu akhir
menit -= kurang_menit
if menit < 0:
    jam -= 1
    menit += 60

jam -= kurang_jam
if jam < 0:
    jam += 24

# Cetak waktu akhir
print(f"Waktu sekarang menunjukkan Pukul {jam:02d}:{menit:02d}")
