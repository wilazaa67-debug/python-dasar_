# Bab 8: Function

print("=== Bab 8: Function ===")

def sapa(nama):
    print(f"Halo {nama}, selamat datang!")

def tambah(a, b):
    return a + b

def hitung_luas_persegi(sisi):
    return sisi * sisi

# Panggil functionnya
sapa("Wiliandri")
sapa("Budi")

hasil = tambah(10, 5)
print(f"10 + 5 = {hasil}")

luas = hitung_luas_persegi(7)
print(f"Luas persegi sisi 7 = {luas}")