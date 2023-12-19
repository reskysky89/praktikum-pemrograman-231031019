nama = 'reski septiawan'
nim= '231031019'
meet= 'praktikum 3'
prodi = 'Sistem Informasi A'
email = 'reskyptwn89@gmail.com'
kota = 'Parepare'
hari = '08 September 2005'
alamat = 'Bau Massepe'
asal = 'Parepare'
hobi = 'Mobile Legends'
tinggi = '160 cm'

print('-' *50)
print(f'{nama.upper().center(50)}')
print(f'{nim.center(50)}')
print()
print()
print(f'{meet.capitalize().rjust(50)}')
print(f'{prodi.title().rjust(50)}')
print(f'{email.rjust(50)}')
print('-' *50)


print(f'    Halo,nama saya {nama.upper()} dengan NIM {nim} \ndari prodi {prodi}, ini adalah file {meet}. \nTerima kasih')

print(f''' Biodata saya, 
Nama\t: {nama.title()}
NIM\t: {nim}
Prodi\t: {prodi.title()}
TTL\t: {kota} {hari}
Alamat\t: {alamat}
Asal\t: {asal}
Hobi\t: {hobi}
Tinggi\t: {tinggi}''')

stat = 'sir issac newtown'
up =stat.upper()
print(up)
up = up.split()
print(up)
print(up[2][0],up[0],up[1])
print(up[2],up[0][0],up[1][0])
print('NEWTON S I')

stat2 = '&sir$ @issac# *newton.'
up2 = stat2.upper()
print(up2)
up2 = up2.split()
print(up2)
print(up2[0][1:-1],up2[1][1:-1],up2[2][1:-1])
#print('N SIR ISSAC')






