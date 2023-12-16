def duplikat(buah):
    hasil= []
    for buah in buah:
        hasil.append(buah)
        hasil.append(buah)
    return hasil

jenis_buah = ["pepaya", "mangga", "pisang", "durian", "jambu"]
hasil = duplikat(jenis_buah)
print(hasil)