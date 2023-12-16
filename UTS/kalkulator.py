# Kalkulator

print(10*"=")
print("Kalkulator")
print(10*"=" + "\n")

bilangan_1 = int(input("Masukkan bilangan 1= "))
operator = input("Operator (+, -, x, /)= ")
bilangan_2 = int(input("Masukkan bilangan 2= "))

# Percabangan

if operator == "+":
    hasil = bilangan_1 + bilangan_2
    print(f"hasilnya adalah {hasil}")
elif operator == "-":
    hasil = bilangan_1 - bilangan_2
    print(f"hasilnya adalah {hasil}")
elif operator == "x" or operator == "*":
    hasil = bilangan_1 * bilangan_2
    print(f"hasilnya adalah {hasil}")
elif operator == "/":
    hasil = bilangan_1 / bilangan_2
    print(f"hasilnya adalah {hasil}")
elif operator == "**":
    hasil = bilangan_1 ** bilangan_2
    print(f"hasilnya adalah {hasil}")
else:
    print("Masukkan data dengan valid!!!")
    
print("Hasil program akhir, Terima Kasih!")




