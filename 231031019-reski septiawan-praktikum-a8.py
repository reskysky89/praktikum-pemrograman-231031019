def layer_one():
    password = "sandi01"
    attempts = 3

    while attempts > 0:
        user_input = input("Masukkan password untuk lapisan pertama: ")
        if user_input == password:
            print("Selamat! Anda berhasil melewati lapisan pertama.")
            return True
        else:
            attempts -= 1
            print(f"Password salah. Percobaan tersisa: {attempts}")

    print("Anda gagal melewati lapisan pertama.")
    return False

def layer_two():
    password = "sandi02"
    attempts = 3

    while attempts > 0:
        user_input = input("Masukkan password untuk lapisan kedua: ")
        if user_input == password:
            print("Selamat! Anda berhasil melewati lapisan kedua.")
            return True
        else:
            attempts -= 1
            print(f"Password salah. Percobaan tersisa: {attempts}")

    print("Anda gagal melewati lapisan kedua.")
    return False

def layer_three():
    password = "sandi03"
    attempts = 3

    while attempts > 0:
        user_input = input("Masukkan password untuk lapisan ketiga: ")
        if user_input == password:
            print("Selamat! Anda berhasil melewati lapisan ketiga.")
            return True
        else:
            attempts -= 1
            print(f"Password salah. Percobaan tersisa: {attempts}")

    print("Anda gagal melewati lapisan ketiga.")
    return False

def main():
    print("Selamat datang di sistem keamanan berlapis!")
    
    if layer_one():
        if layer_two():
            if layer_three():
                print("Selamat! Anda berhasil melewati semua lapisan keamanan.")

main()
