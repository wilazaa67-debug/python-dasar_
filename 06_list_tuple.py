# Bab 6: List & Tuple

print("=== Bab 6: List & Tuple ===")

# List - Bisa diubah
hobi = ["Ngoding", "Gaming", "Makan"]
print(f"Hobi awal: {hobi}")

hobi.append("Tidur")
print(f"Setelah tambah Tidur: {hobi}")

hobi.remove("Gaming")
print(f"Setelah hapus Gaming: {hobi}")

print(f"Jumlah hobi: {len(hobi)}")
print(f"Hobi pertama: {hobi[0]}")

# Tuple - TIDAK bisa diubah
koordinat = (10, 20)
print(f"\nKoordinat: {koordinat}")
print(f"X: {koordinat[0]}, Y: {koordinat[1]}")