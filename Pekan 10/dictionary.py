data_diri = {"nama":"Dono", "Mapel":"Indo"}

#Mengakses dictionary
print(data_diri["nama"])

#Menambah item
data_diri["jurusan"] = "Teknik Informatika"
print(data_diri)

#Update item
data_diri["nama"]= "Kasino"
print(data_diri)

#Menghapus item
data_diri.pop("Mapel")
print(data_diri)

#Cek keberadaan key
if "nama" in data_diri:
    print("Terdapat nama")
else:
    print("Tidak ada nama")