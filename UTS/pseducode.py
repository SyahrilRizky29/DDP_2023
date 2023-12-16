# Pseudocode Luas dan Keliling Trapesium

print(''' 
menghitung luas bangun datar
1 = Keliling trapesium
2 = Luas trapesium
      ''')

luasdankeliling =int(input('pilihlah rumus:'))
sisi1 =int(input("Masukkan Nilai Sisi  1: "))
sisi2 =int(input("Masukkan Nilai Sisi  2: "))
sisi3 =int(input("Masukkan Nilai Sisi  3: "))
sisi4 =int(input("Masukkan Nilai Sisi  4: "))
tinggi =int(input("Masukkan Nilai Tinggi: "))

match luasdankeliling:
    case 1:
        keliling =int(sisi1+sisi2+sisi3+sisi4)
        print('Keliling trapesium adalah',keliling)
    case 2:
       luas =int(sisi1+sisi3*tinggi/2)
       print('Luas trapesium adalah',luas)
    case _:
        print('salah pilih')