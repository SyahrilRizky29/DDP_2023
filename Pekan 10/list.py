buah = ['rambutan', 'jambu', 'mangga', 'pepaya', 'pisang']

#jika plus dihitung dari kiri, jika min dari kanan
buah[1 -1]

#Menampilkan panjang list
print(len(buah))

#Cek keberadaan nilai
if "jambu" in buah:
    print("Terdapat jambu")
else:
    print("Tidak ada jambu")

#Looping list
for fruits in buah:
    print(fruits)