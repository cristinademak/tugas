def hitung_luas_segitiga(alas, tinggi):
    luas = 0.5 * alas * tinggi
    return luas

# Masukkan nilai alas dan tinggi dari segitiga
alas = float(input("Masukkan panjang alas segitiga: "))
tinggi = float(input("Masukkan tinggi segitiga: "))

# Hitung luas segitiga
luas_segitiga = hitung_luas_segitiga(alas, tinggi)
print("Luas segitiga adalah:", luas_segitiga)