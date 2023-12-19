nim = ['2','3','1','0','3','1','0','1','9']
# nim2 = '231031019'
print(nim[1:3])
# print(nim2[1:3])

#akses item
print(f'item indeks 0: {nim[0]}')
print(f'item indeks 4: {nim[4]}')
print(f'item indeks terakhir: {nim[len(nim)-1]}')

#akses indeks negatif
print(f'item indeks terakhir: {nim[-1]}')
print(f'item indeks pertama: {nim[-len(nim)]}')
print(f'item indeks 6 [-3]: {nim[-3]}')
print(f'item indeks 4 [-5]: {nim[-5]}')
print(f'item indeks 7 [-2]: {nim[-2]}')

# aksess indeks batas
print(f'item indeks  1,2,....: \n {nim[1:]}')
print(f'item indeks  3,4,,....: \n {nim[3:]}')
print(f'item indeks  0,1,2,....: \n {nim[:3]}')
print(f'item indeks  0,1,2,3,....: \n {nim[:4]}')
print(f'item indeks  semua: \n {nim[:]}')
print(f'item indeks  [:8]: \n {nim[:-1]}')
print(f'item indeks  [:6]: \n {nim[:-3]}')

# pengirisan
print(f'item indeks  1,2: \n {nim[1:3]}')
print(f'item indeks  2,3,4: \n {nim[2:5]}')
print(f'item indeks  kosong: \n {nim[3:3]}')
print(f'item indeks [8:8] kosong: \n {nim[-1:-1]}')
print(f'item indeks [1:8] : \n {nim[1:-1]}')
print(f'item indeks [2:7] : \n {nim[2:-2]}')

#latihan list

data = ['Reski Septiawan',2023,'Aktif']
nilai= [99,98,97,95]

print('Nama: '+ data[0])
print('angkatan:', data[1])
print('status: '+ data[2])

print(f'Nama: {data[0]}, status kuliah : {data[2]}')
print(f'Data terbesar adalah: {max(nilai)}')
print(f'Data terkecil adalah: {min(nilai)}')
print(f'Rata rata nilai  adalah: {sum(nilai) / len(nilai)}')

#tuple
data2 = ('Reski septiawan',2023,'Aktif')
nilai2= (90,89,93,97)

print(data[1])
print(data[-1])
print(nilai[1:-1])

print(f'Jumlah nilai mahasiswa adalah : {sum(nilai2)}')
print(f'Data terbesar nilai adalah : {max(nilai2)}')
print(f'Data terkecil nilai adalah : {min(nilai2)}')
print(f'Rata rata nilai adalah : {sum(nilai2) / len(nilai2)}')
#Latihan Nested list
data3 = [['Reski ',2023,'Aktif'],
[90,89,93,97],
[20,22],
['S1-Reguler','Ganjil']]
matkul = ['Sainster','Kaldas','PROG','Agama']
sks = [2,3,3,2]
#tugas tambahkan matkul dan sks ke dalam data (di akhir) terjawab
data3.append(matkul)
data3.append(sks)
print(data3)
data3[4].append('PTI')
data3[4].append('Pancasila')
data3[4].append('CINTA')
data3[4].append('Bahasa')
print(data3)
# mata kuliah 1; matkul1 dengan jumlah sks2
print(f'mata kuliah 1 : {data3[4][0]} dengan jumlah {data3[5][0]} sks')
# mata kuliah 2: matkul2 dengan sks 3
print(f'mata kuliah 2 : {data3[4][1]} dengan jumlah {data3[5][1]} sks')
# mata kuliah 3: matkul3 dengan sks 3
print(f'mata kuliah 3 : {data3[4][2]} dengan jumlah {data3[5][1]} sks')
# mata kuliah 4: matkul4 dengan sks 2
print(f'mata kuliah 4 : {data3[4][3]} dengan jumlah {data3[5][0]} sks')
print(f'mata kuliah 5 : {data3[4][4]} dengan jumlah {data3[5][1]} sks')
print(f'mata kuliah 6 : {data3[4][5]} dengan jumlah {data3[5][1]} sks')
print(f'mata kuliah 7 : {data3[4][6]} dengan jumlah {data3[5][0]} sks')
print(f'mata kuliah 8 : {data3[4][7]} dengan jumlah {data3[5][0]} sks')
# Tambahkan 4 matkul dengan sks nya
print(data3[0][0])
print(data3[3][0])
print(data3[2][0:])

# tugas nama mahasiswa dengan nim
# >> Program pendidikan Thomas: S1-Reguler
print(f'Program pendidikan {data3[0][0]}: {data3[3][0]}')
# >> Angkatan : 2023-Ganjil
print(f'Angkatan {data3[0][1]}: {data3[3][1]}')
# >> Jumlah nilai Thomas adalah: 4
print(f'Jumlah nilai {data3[0][0]} adalah: {len(data3[1])}')
# >> Data terbesar Thomas adalah: 97
print(f'Data terbesar {data3[0][0]} adalah : {max(data3[1])}')
# >> Data terkecil Thomas adalah: 89
print(f'Data terkecil {data3[0][0]} adalah : {min(data3[1])}') 

# >> Rata-rata nilai Thomas adalah: 92.25
print(f'Rata rata nilai {data3[0][0]} adalah : {sum(data3[1]) / len(data3[1])}') 


























