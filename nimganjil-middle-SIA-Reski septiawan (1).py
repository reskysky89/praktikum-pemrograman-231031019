''' UTS
1. Buat variabel jenis list berikut.
    
    Bio =  ['Institut Teknologi Bacharuddin Jusuf Habibie',
            'Parepare',
            'Jurusan Sains',
            'kartu hasil studi mahasiswa',
            'Nama Lengkap',
            'NIM',
            'S1',
            'Sistem Informasi A',
            '2023-2024',
            'ganjil',
            'aktif',
            'Tanggal-Bulan-Tahun Lahir']
#(NOTED: sesuaikan dengan data anda)


2. Buat variabel nested list berikut.

MK =   [['Matkul1','Matkul2','Matkul3','Matkul4','Matkul5','Matkul6','Matkul7','Matkul8'],
        [3,2,3,2,3,3,3,2],
        ['22A1209','22A1210','22A1211','22A1212','22A1213','22A1214','22A1215','22A1216'],
        [3.50,3.00,3.75,4.00,3.75,3.50,3.75,3.00]]

#(NOTED: Ubah Nama Matakuliah, Jumlah SKS, dan Nilai)

3. Buat Kode dengan hasil runing seperti berikut.


            INSTITUT TEKNOLOGI BACHARUDDIN JUSUF HABIBIE
                           JURUSAN SAINS
                    KARTU HASIL STUDI MAHASISWA
                          GANJIL 2023/2024

                    
Nama Lengkap    : NAMA LENGKAP
NIM             : NIM
Program/Prodi   : S1/Sistem Informasi A
Tahun Masuk     : 2023-Ganjil
Status          : Aktif
|--|--   12   --|--             31            --|-- 7 --|--    13   --|
-----------------------------------------------------------------------
No. Kode        |           Mata Kuliah         |  SKS  | Nilai (0-4) |
-----------------------------------------------------------------------
1   22A1209     | Matkul1                       |   3   |         3.50|
2   22A1210     | Matkul2                       |   2   |         3.00|
3   22A1211     | Matkul3                       |   3   |         3.75|
4   22A1212     | Matkul4                       |   2   |         4.00|
5   22A1213     | Matkul5                       |   3   |         3.75|
6   22A1214     | Matkul6                       |   3   |         3.50|
7   22A1215     | Matkul7                       |   3   |         3.75|
8   22A1216     | Matkul8                       |   2   |         3.00|
-----------------------------------------------------------------------
                                       TOTAL SKS:   21
-----------------------------------------------------------------------
|---------------------------------71-----------------------------------|
Summary:
Jumlah Mata Kuliah : 8 Mata Kuliah
Nilai Tertinggi    : 4.00  (22A1212 - Matkul4)
Nilai Terendah     : 3.00  (22A1211 - Matkul2)
IP Kumulatif       : 3.00
                                   
                                               Parepare, 25 Oktober 2023



                                                     NAMA LENGKAP      
                                                     ------------
'''



# Tulis Kode Jawaban di bawah!

Bio =  ['Institut Teknologi Bacharuddin Jusuf Habibie',
            'Parepare',
            'Jurusan Sains',
            'kartu hasil studi mahasiswa',
            'Reski Septiawan',
            '231031019',
            'S1',
            'Sistem Informasi A',
            '2023-2024',
            'ganjil',
            'aktif',
            '08-september-2005']

MK =   [['PROG','PTI','CINTA','KALDAS','SAINSTER','AGAMA','BAHASA','PANCASILA'],
        [3,2,3,2,3,3,3,2],
        ['22A1209','22A1210','22A1211','22A1212','22A1213','22A1214','22A1215','22A1216'],
        [3.50,3.00,3.75,4.00,3.75,3.50,3.75,3.00]]


# Data biodata
nama_lengkap, nim, program_prodi, tahun_masuk, status = Bio[4:9]

# Data khs
matakuliah, sks, kode_matakuliah, nilai = MK

# Menampilkan header
header1 = Bio[0].upper().center(71)
header2 = Bio[2].upper().center(71)
header3 = Bio[3].upper().center(71)
header4 = f"{Bio[9].upper()} {Bio[8]}".center(71)

print(header1)
print(header2)
print(header3)
print(header4)
print()
print()
print(f"Nama Lengkap    : {nama_lengkap}\nNIM             : {nim}\nProgram/Prodi   : {Bio[6]}/{Bio[7]}\nTahun Masuk     : {Bio[8]}\nStatus          : {Bio[10]}\n|--|--   12   --|--             31            --|-- 7 --|--    13   --|")
print("-" * 71)
print("Summary:")
print(f"Jumlah Mata Kuliah : {len(matakuliah)} Mata Kuliah")
print(f"Nilai Tertinggi    : {max(nilai):.2f}  ({kode_matakuliah[nilai.index(max(nilai))]} - {matakuliah[nilai.index(max(nilai))]})")
print(f"Nilai Terendah     : {min(nilai):.2f}  ({kode_matakuliah[nilai.index(min(nilai))]} - {matakuliah[nilai.index(min(nilai))]})")
print(f"IP Kumulatif       : {sum(nilai) / len(nilai):.2f}")
print("\n")
print(f"{Bio[1]}, {Bio[-1]}\n\n")
print(f"{nama_lengkap.upper()}")

