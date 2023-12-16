# 2 Buat program python dgn match case untuk
# menghitung luas bangunan datar :
# jika pilih 1, maka menghitung luas persegi
# jika pilih 2, maka menghitung luas lingkaran
# jika pilih 3, maka menghitung luas segitiga
# selain pilihan di atas, maka keterangan : salah pilih angka
# bil1 = 3.14
# bil2 = 10
# hasil = bil1 * bil2
# print(int(hasil))

#bil1 = 3.14
#bil2 = 100
#hasil = bil1 * bil2
#print(type(bil1))
#print(type(bil2))
#print(type(hasil))

print(''' 
menghitung luas bangun datar
1 = luas persegi
2 = luas lingkaran
3 = luas segitiga
      ''')

bangunandatar = int (input("Masukkan bangunan datar:"))

match bangunandatar:
    case 1:
        sisi = int (input("Masukkan nilai sisi:"))
        luaspersegi = int (sisi*sisi*sisi)
        print("luas persegi" "untuk", sisi,"adalah", luaspersegi)
    case 2:
        jarijari = int (input("Masukkan jarijari:"))
        luaslingkaran = int (3.14 * jarijari * jarijari)
        print("luas lingkaran", jarijari, "adalah", luaslingkaran)
    case 3:
        alas = int (input("Masukkan alas:"))
        tinggi = int (input("Masukkan tinggi:"))
        luassegitiga = int (1.2*alas*tinggi)
        print("luas segitiga", alas, "dan tinggi", tinggi, "adalah: 3", luassegitiga)
    case _:
        print("Pilihan yang anda masukkan salah!!!")