class fitur:
    def __init__(self, masukan_pin, saldo=0, pin= 3003):
        self.masukan_pin = masukan_pin 
        self.saldo = saldo
        self.pin = pin

    def cek_pin (self):
        return self.pin
    
    def mengecek_pin(self):
        masukan_pin = int(input ('Masukkan PIN anda: '))

        if masukan_pin == int(self.cek_pin()):
            print('PIN anda benar! Anda berhasil masuk!')
            return "benar"
            
        else: 
            print('PIN anda salah. Mengeluarkan anda dari menu')
            self.exit()
    
    def cek_saldo(self):
        print("Saldo anda saat ini adalah ", self.saldo)
    
    def deposit(self, jumlah):
        self.saldo += jumlah
        print("Anda berhasil menyetor uang sebesar ", jumlah)
    
    def tarik(self, jumlah):
        if self.saldo >= jumlah:
            self.saldo -= jumlah
            print("Anda berhasil menarik uang sebesar ", jumlah)
        else:
            print("Saldo anda tidak cukup!")
    
    def ganti (self):
        self.pin = input('Masukkan pin baru anda: ')
        
    def exit(self):
        print("Terimakasih telah menggunakan layanan kami! Semoga hari anda menyenangkan")
        exit()