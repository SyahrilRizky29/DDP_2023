def persegi(sisi):
    luas = sisi * sisi
    keliling = 4 * sisi
    print("Luas persegi: ", luas)
    print("Keliling persegi: ", keliling)
    
    
def persegi_panjang(panjang, lebar):
    luas = panjang * lebar
    keliling = 2 * (panjang + lebar)
    print("Luas persegi panjang: ", luas)
    print("Keliling persegi panjang: ", keliling)
    
def lingkaran(jari2):
    phi = 3.14
    luas = phi * jari2 * jari2
    keliling = 2 * phi * jari2
    print("Luas Lingkaran: ", luas)
    print("Keliling Lingkaran: ", keliling)
    
    
def segitiga_sama_sisi(alas, tinggi):
    luas = 0.5 * alas * tinggi
    keliling = alas * 3
    print("Luas Segitiga sama sisi: ", luas)
    print("Keliling Segitiga sama sisi: ", keliling)
      
def layang2(diagonal1, diagonal2, sisi_atas, sisi_bawah):
    luas = diagonal1 * diagonal2 * 0.5  
    keliling = sisi_atas * sisi_bawah * 2
    print("Luas layang2: ", luas)
    print("Keliling layang2: ", keliling)
    
def belah_ketupat(diagonal1, diagonal2, sisi):
    luas = 0.5 * diagonal1 * diagonal2
    keliling = 4 * sisi
    print("Luas Belah Ketupat: ", luas)
    print("Keliling Belah Ketupat: ", keliling)
      
def jajar_genjang(alas, tinggi, sisi_miring):
    luas = alas * tinggi
    keliling = 2 * alas + sisi_miring
    print("Luas Jajar Genjang: ", luas)
    print("Keliling Jajar Genjang: ", keliling)
    

