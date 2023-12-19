print('praktikum-a2\n')

print('NAMA   :RESKI SEPTIAWAN')
print('NIM    :231031019')
print('Prodi  :SISTEM INFORMASI A\n')

# INI OPERATOR ASSIGMENT
a = 19
print('Nilai a adalah',a)
a += 3
print('Nilai a+3 adalah',a)
a = 19

print('Nilai a adalah',a)
a -= 3
print('Nilai a-3 adalah',a)

a = 19
print('Nilai a adalah',a)
a *= 2
print('Nilai a*2 adalah',a)

a = 19
print('Nilai a adalah',a)
a /= 2
print('Nilai a/2 adalah',a)

a = 3
print('Nilai a adalah',a)
a **= 2
print('Nilai a**2 adalah',a)

a = 35
print('Nilai a adalah',a)
a %= 32
print('Nilai a%32 adalah',a)

a = 35
print('Nilai a adalah',a)
a //= 32
print('Nilai a//32 adalah',a)

a = 35
print('Nilai a adalah',a)
a &= 32
print('Nilai a&32 adalah',a)

a = 35
print('Nilai a adalah',a)
a |= 32
print('Nilai a|32 adalah',a)

a = 35
print('Nilai a adalah',a)
a ^= 32
print('Nilai a^32 adalah',a)

a = 35
print('Nilai a adalah',a)
a>>= 32
print('Nilai >>32 adalah',a)

a = 35
print('Nilai a adalah',a)
a <<= 32
print('Nilai a<<32 adalah',a)




# Tugas melanjutkan untuk operator selanjutnya

#OPERATOR PERBANDINGAN
a = 9
b = 13
print('\n-------- Besar dari 19')
hasil = a >19
print(a,">19 adalah",hasil)
hasil = b > 19
print(b,">19 adalah",hasil)

print('\n-------- Kecil dari 19')
hasil = a < 19
print(a,"<19 adalah",hasil)
hasil = b < 19
print(b,"<19 adalah",hasil)

print('\n-------- Besar besar atau sama dari 19')
#INI TUGAS
# hasil = a >=
hasil = a >= 19
print(a,">=19 adalah",hasil)
#hasil = b >=
hasil = b >= 19
print(b,">=19 adalah",hasil)

print('\n-------- kecil atau sama dari 19')
# hasil = a <=
hasil = a <= 19
print(a,"<=19 adalah",hasil)
#hasil = b <=
hasil = b <= 19
print(b,"<=19 adalah",hasil)

print('\n--------  sama dari 19')
# hasil = a ==
hasil = a == 19
print(a,"==19 adalah",hasil)
#hasil = b ==
hasil = b == 19
print(b,"==19 adalah",hasil)

print('\n-------- Tidak sama sama dari 19')
# hasil = a !=
hasil = a != 19
print(a,"!=19 adalah",hasil)
#hasil = b !=
hasil = b != 19
print(b,"!=19 adalah",hasil)

#OPERATOR LOGIKA
a = True
b = False
print("\n=======AND=========")
hasil = a and a
print(a,"and",a, 'hasilnya=',hasil)

hasil = a and b
print(a,"and",b, 'hasilnya=',hasil)

hasil = b and a
print(b,"and",a, 'hasilnya=',hasil)

hasil = b and b
print(b,"and",b, 'hasilnya=',hasil)


print("\n=======OR=========")
#tugas hasil = a or a
hasil = a or a
print(a,"or",a, 'hasilnya=',hasil)
#tugas hasil = a or b
hasil = a or b
print(a,"or",b, 'hasilnya=',hasil)
#tugas hasil = b or a
hasil = b or a
print(b,"or",a, 'hasilnya=',hasil)
#tugas hasil = b or b
hasil = b or b
print(b,"or",b, 'hasilnya=',hasil)

print("\n=======XOR=========")
hasil = a ^ a
print(a,"xor",a, 'hasilnya=',hasil)

hasil = a ^ b
print(a,"xor",b, 'hasilnya=',hasil)

hasil = b ^ a
print(b,"xor",a, 'hasilnya=',hasil)

hasil = b ^ b
print(b,"xor",b, 'hasilnya=',hasil)

print("\n=======NOT=========")
hasil = not a 
print("not",a, 'hasilnya=',hasil)

hasil = not b
print("not",b, 'hasilnya=',hasil)

#OPERATOR MEMBERSHIP
print('\n==========IN======')
nama = 'Reski Septiawan'

test = 'aw'
cek = test in nama
print(test,'terdapat di',nama,'adalah',cek)

test = 'wa'
cek = test in nama
print(test,'terdapat di',nama,'adalah',cek)
print()
test1 = 'a'
test2 = 'i'
test3 = 'u'
test4 = 'e'
test5 = 'o'

cek = test1 in nama
print(test1,'terdapat di',nama,'adalah',cek)
cek = test2 in nama
print(test2,'terdapat di',nama,'adalah',cek)
cek = test3 in nama
print(test3,'terdapat di',nama,'adalah',cek)
cek = test4 in nama
print(test4,'terdapat di',nama,'adalah',cek)
cek = test5 in nama
print(test5,'terdapat di',nama,'adalah',cek)
print('\n=========NOT IN======')
#Tugas lanjutkan untuk NOT iN dengan cara yang sama
nama = 'Reski Septiawan'
test = 'aw'
cek = test not in nama
print(test,'terdapat di',nama,'adalah',cek)
test = 'wa'
cek = test not in nama
print(test,'terdapat di',nama,'adalah',cek)
print()
test1 = 'a'
test2 = 'i'
test3 = 'u'
test4 = 'e'
test5 = 'o'

cek = test1 not in nama
print(test1,'terdapat di',nama,'adalah',cek)
cek = test2 not in nama
print(test2,'terdapat di',nama,'adalah',cek)
cek = test3 not in nama
print(test3,'terdapat di',nama,'adalah',cek)
cek = test4 not in nama
print(test4,'terdapat di',nama,'adalah',cek)
cek = test5 not in nama
print(test5,'terdapat di',nama,'adalah',cek)


































