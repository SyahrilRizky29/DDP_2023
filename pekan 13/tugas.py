class Hewan:
    def __init__(self, nama, makanan, habitat, berkembangbiak):
        self.nama = nama
        self.makanan = makanan
        self.habitat = habitat
        self.berkembangbiak = berkembangbiak

    def info(self):
        print("nama\t:", self.nama)
        print("makanan\t:", self.makanan)
        print("habitat\t:", self.habitat)
        print("berkembangbiak\t:", self.berkembangbiak)

class Kuda(Hewan):
    def __init__(self, nama, habitat):
        super().__init__(nama, "Rumput", habitat, "Vivipar")

    def lari(self):
        print("Hiiihaaaa....!!!")
        print("==========================================")
        print()


class Anjing(Hewan):
    def __init__(self, nama, habitat):
        super().__init__(nama, "Cilok", habitat, "Vivipar")

    def suara(self):
        print("Auugggggg... ^o^")
        print("==========================================")
        print()


class Kucing(Hewan):
    def __init__(self, nama, habitat):
        super().__init__(nama, "Endog", habitat, "Vivipar")

    def suara(self):
        print("Miawww... >//< ")
        print("==========================================")
        print()
        
# Contoh Penggunaan

kuda = Kuda("Kuda Morgan", "Padang Rumput")
anjing = Anjing("Paus Orca", "Lautan")
kucing = Kucing("Kucing Persia", "Rumah")

kuda.info()
kuda.lari()

anjing.info()
anjing.suara()

kucing.info()
kucing.suara()