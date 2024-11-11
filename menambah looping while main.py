def menu_login():
    username = "Daspro2024"
    password_benar = "Latihan"
    
    kesempatan = 3
    
    print("Selamat datang di menu login!")
    print(f"Username: {username}")
    while kesempatan > 0:
        password_input = input("Masukkan password: ")
        
        if password_input == password_benar:
            print("Login berhasil! Selamat datang.")
