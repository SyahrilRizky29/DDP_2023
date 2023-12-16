motor= {"Beat", "Honda", "Vario"}
mobil= {"Bajaj", "Ferrari","Truk"}
print(motor)

#Nambah Item
motor.add("Nmax")
print(motor)

#Hapus Item
motor.remove("Beat")
print(motor)

#Union
kendaraan = motor.union(mobil)
print(kendaraan)

#Update
motor.update(mobil)
print(motor)