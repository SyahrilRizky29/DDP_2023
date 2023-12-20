class Orang:
    def __init__(self, fnama, lnama):
        self.fnama = fnama
        self.lnama = lnama
        
    def makan(self):
        print("saya bisa makan")
        
    def cetak(self):
        print("nama saya ", self.fnama, self.lnama)
        
class Mahasiswa(Orang):
    def __init__(self, fnama, lnama, prodi, angkatan):
        super().__init__(fnama, lnama)
        self.prodi = prodi
        self.angkatan = angkatan
        
    def cetak(self):
        super().cetak()
        print("saya prodi ", self.prodi, "angkatan ", self.angkatan)
        
class Pegawai(Orang):
    def bekerja(self):
        print("saya bekerja")
        
# Objek Orang
x = Orang("Bagus", "Maulana")
x.cetak()

#x.bekerja()

# objek mahasiswa
y = Mahasiswa("Dwi", "Astuti", "Teknik Informatika", 2023)
y.cetak()
y.makan()

# objek pegawai
agus = Pegawai("Agus", "Rahman")
agus.bekerja()
