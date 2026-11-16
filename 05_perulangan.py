# Bab 5: Perulangan

print("=== Bab 5: Perulangan ===")

print("--- For Loop 1 sampai 5 ---")
for i in range(1, 6):
    print(f"Perulangan ke-{i}")

print("--- While Loop ---")
angka = 1
while angka <= 5:
    print(f"Angka: {angka}")
    angka += 1

print("--- Loop List Buah ---")
buah = ["Apel", "Mangga", "Jeruk", "Pisang"]
for b in buah:
    print(f"Saya suka {b}")