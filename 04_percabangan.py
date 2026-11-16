# Bab 4: Percabangan / If Else

nilai = 85

print("=== Bab 4: Percabangan ===")
print(f"Nilai kamu: {nilai}")

if nilai >= 90:
    print("Grade: A, Mantap!")
elif nilai >= 80:
    print("Grade: B, Bagus!")
elif nilai >= 70:
    print("Grade: C, Lumayan!")
else:
    print("Grade: D, Belajar lagi ya!")

# Cek ganjil genap
angka = 10
if angka % 2 == 0:
    print(f"{angka} adalah bilangan GENAP")
else:
    print(f"{angka} adalah bilangan GANJIL")