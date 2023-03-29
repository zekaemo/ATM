from fitur import fitur
print('ATM')
print("Selamat datang!")

atm = fitur(id)

def menu():

    while True:  # supaya selalu berulang tanpa stop

        atm.mengecek_pin()

        while "benar":
            
            print("""
            Menu ATM:
            1. Cek saldo
            2. Setor tunai
            3. Tarik tunai
            4. Ganti PIN
            5. Keluar
            """)

            pilihan = int(input("Apa yang bisa kami bantu? "))
            if pilihan == 1:
                atm.mengecek_pin()

                if "benar":
                    atm.cek_saldo()

            elif pilihan == 2:
                atm.mengecek_pin()
                
                if "benar":
                    jumlah = int(input("Masukkan nominal uang yang ingin anda setor: "))
                    atm.deposit(jumlah)

            elif pilihan == 3:
                atm.mengecek_pin()
                
                if "benar":
                    jumlah = int(input("Masukkan nominal uang yang ingin anda tarik: "))
                    atm.tarik(jumlah)
            elif pilihan == 4:
                atm.mengecek_pin()
                
                if "benar":
                    atm.ganti()
            elif pilihan == 5:
                atm.exit()
            else:
                print("Kata kunci tidak dikenali. Coba lagi!")

if __name__ == "__main__":  # nama module scr otomatis diberikan oleh python dengan nama "main"
    menu()
