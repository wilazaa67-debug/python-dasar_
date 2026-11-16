# Bab 10: Error Handling

print("=== Bab 10: Error Handling ===")

try:
    angka1 = int(input("Masukkan angka pertama: "))
    angka2 = int(input("Masukkan angka kedua: "))

    hasil = angka1 / angka2
    print(f"Hasil {angka1} / {angka2} = {hasil}")

except ZeroDivisionError:
    print("Waduh! Tidak bisa dibagi 0 bre!")

except ValueError:
    print("Waduh! Harus masukin angka, bukan huruf!")

except Exception as e:
    print(f"Ada error lain: {e}")

else:
    print("Program berjalan lancar, tanpa error!")

finally:
    print("Program selesai, makasih udah nyoba!")