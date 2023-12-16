# 1. buatlah fungsi untuk menampilakan data diri :
# contoh pemanggilan : profil(nama, alamat, gender, umur, hoby)

# 2. buatlah fungsi untuk mencari kelulusan nilai dari berikut : 
# jika nilai < 60 maka gagal 
# jika nilai = 61 - 70 maka baik 
# jika nilai = 71 - 80 maka sangat baik 
# jika nilai = 81 - 100 maka istimewa 

# ex:
# nilai (60)

# 3. buatlah fungsi untuk mencetak nilai bilangan ganjil dari parameter yang di masukan :
# ex : ganjil (100)

# Profil
def profil(nama, alamat, gender, umur, hobby):
    print("Nama saya", nama)
    print("Tinggal di", alamat)
    print("Saya", gender)
    print("umur saya", umur)
    print("hobby saya", hobby)
profil("Aril", "Bogor", "Pria", "21", "Live Streaming")

# nilai ujian
nilai = int(input("Masukkan nilai= "))
def hasil_ujian(nilai):
    if nilai < 60:
        return "Failed"
    elif nilai <= 70:
        return "Not badlah"
    elif nilai <= 80:
        return "GG Gemink"
    elif nilai <= 100:
        return "Sepuh"
    else:
        return "Yang bener dong!"
    
print(hasil_ujian(nilai))

# menentukan bilangan ganjil
def bil_ganjil(z):
    for z in range(1, 100):
        if z % 2 == 1:
            print("Angka ganjil ditemukan! ", z)
bil_ganjil(100)
    

# def cari_ganjil(*angka):
#     for i in angka:
#         if i % 2 == 1:
#             print("Angka ganjil ditemukan: ", i)
#             return
        
# cari_ganjil(2, 884, 974, 276, 798, 123, 776, 13, 871)
