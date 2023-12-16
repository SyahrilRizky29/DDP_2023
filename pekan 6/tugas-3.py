# Buat program untuk minta input jumlah baris dan buat
# rangkaian berikut ini
# *
# **
# ***
# ****
# ● Dan seterusnya sejumlah baris yang diinputkan
# ● Gunakan for loop dengan range

input= int(input("Masukkan jumlah= "))
for i in range(1, input+1):
    for a in range(i):
        print("*", end=" ")
    print()