# Bab 9: Input dari User

print("=== Bab 9: Input dari User ===")

nama = input("Masukkan nama kamu: ")
umur = int(input("Masukkan umur kamu: "))
kota = input("Masukkan kota kamu: ")

print(f"\nHalo {nama}!")
print(f"Kamu umur {umur} tahun, tinggal di {kota}.")

tahun_lahir = 2026 - umur
print(f"Berarti kamu lahir tahun {tahun_lahir} ya?")

if umur >= 17:
    print("Kamu sudah bisa bikin KTP!")
else:
    print("Kamu belum bisa bikin KTP, sabar ya!")