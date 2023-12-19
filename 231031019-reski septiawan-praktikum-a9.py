def judul():
    print('PROGRAM MENGHITUNG LUAS DAN KELILING'.center(45,'-'))
    print('BANGUN DATAR PERSEGI\n'.center(45))

def inputan ():
    panjang = float(input('Masukkan Panjang: '))
    lebar = float(input('Masukkan lebar: '))
    return panjang,lebar
def hitung(panjang,lebar):
    luas = panjang*lebar
    kel = (panjang*lebar)*2
    return luas,kel
def tampil(pesan,nilai):
    print(f'Hasil perhitungan nilai {pesan}: {nilai}')
def pilihan():
    pilih = input ('Apakah ingin lanjut? [y/n]')
    if pilih == 'y':
        a = True
    else:
        a = False
        print('Sampai Jumpa')
    return a
a = True
while a:
    judul() #judul
    panjang,lebar = inputan()     #inputan panjang dan lebar
    luas,kel = hitung(panjang,lebar) # hitung luas dan keliling
    
    tampil('luas',luas)           #pilihan
    tampil('keliling',kel)
    a = pilihan()

