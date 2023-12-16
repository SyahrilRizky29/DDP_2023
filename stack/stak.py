bilangan = [12, 13, 14]

bilangan.append(15)
bilangan.append(30)
print(bilangan)

bilangan.pop()
bilangan.pop()

# queue

bilangan = [1,2,3]

# enqueue
bilangan.append(4)
print(bilangan)

#dequeue
bilangan.pop(0)
print(bilangan)

# set
motor = {"Beat", "Scoopy", "Vario", "Aerox"}
print(motor)
mobil = {"Lamborghini", "GTR", "Ferrari", "Mustang", "Alphart"}

# Menambahkan item
motor.add("Nmax")
print(motor)

# Menghapus item
motor.remove("Beat")
print(motor)

# Menggabungkan Set
kendaraan = motor.union(mobil)
print(kendaraan)

# Update set
motor.update(mobil)
print(motor)

# Dictionary
data_diri = {"nama":"Reza", "mapel":"DDP"}

# Mengakses Dictionary
print(data_diri['nama'])

# Menambah Item
data_diri["jurusan"] = "Teknik Informatika"
print(data_diri)

# Update item
data_diri["nama"] = "Aril Mikhailovna"
print(data_diri)

# Menghapus item
data_diri.pop("mapel")
print(data_diri)

# Cek keberadaan key
if "nama" in data_diri:
    print("Terdapat nama")
else:
    print("Tidak ada nama")
    
# List
fruits = ['banana', 'manggo', 'orange', 'apple', 'star fruits']

# Menampilkan panjang list
print(len (fruits))

# cek keberadaan ilai
if "apple" in fruits:
    print("terdapat apple")
else:
    print("Gk ada apple")

# Looping list
for buah in fruits:
    print(buah)
    
# Tuple
zoo = ('python', 'elephant', 'penguin')
new_zoo = 'monkey', 'camel', zoo
print(new_zoo[2][2])

# Sequence : List, tuple, string
fruits = ['banana', 'manggo', 'orange', 'apple', 'star fruits']
motor = ("Beat", "Scoopy", "Vario", "Aerox")
nama = "Aril Mikhailovna"

#print(fruits[2])
#print(motor[2])

# slicing
print(nama[4:])
print(nama[:-3:2])

