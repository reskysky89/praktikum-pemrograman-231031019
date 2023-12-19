pswr = 'ayangku'
percobaan = 3
a = True
while a:
    masukkan =input('Masukkan password: ')
    if masukkan == pswr:
        print('Selamat anda login')
        a = False
    else:
        if percobaan == 0:
            print('password yang anda masulkkan salah! \n Akun anda terkunci')
            a = False
        else:
            print('password anda masih salah, Sisa percobaan : ', percobaan)
            percobaan -= 1