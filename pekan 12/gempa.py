class gempa:
    lokasi =""
    skala = 0

    def __init__(self, lokasi, skala):
        self.lokasi = lokasi
        self.skala = skala
        
    def dampak(self):
        if self.skala < 3:
             print (f"Dampak gempa di {self.lokasi} : Terasa getaran kecil")
        elif 2 <= self.skala < 5:
             print (f"Dampak gempa di {self.lokasi} : Menggetarkan barang-barang dan suara gaduh")
        elif 4 <= self.skala < 6:
             print (f"Dampak gempa di {self.lokasi} : Kerusakan bangunan")
        elif self.skala >= 7:
             print (f"Dampak gempa di {self.lokasi} : Menimbulkan tsunami")
        else:
             print ("Skala gempa di  tidak valid")

lokasi1 = gempa("Jakarta", 1.8)
lokasi2 = gempa("Lombok", 5.4)
lokasi3 = gempa("Palu", 7.0)
lokasi4 = gempa("Bengkulu", 5.0)
lokasi5 = gempa("Bali", 4.8)