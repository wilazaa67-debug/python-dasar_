# Bab 7: Dictionary

print("=== Bab 7: Dictionary ===")

# Dictionary itu kayak KTP, ada key : value
siswa = {
    "nama": "Wiliandri",
    "umur": 17,
    "kelas": "11 RPL",
    "hobi": "Ngoding"
}

print(f"Data Siswa: {siswa}")
print(f"Nama: {siswa['nama']}")
print(f"Umur: {siswa['umur']}")

# Tambah data baru
siswa["sekolah"] = "SMK Negeri 1"
print(f"Setelah tambah sekolah: {siswa}")

# Ubah data
siswa["umur"] = 18
print(f"Setelah ulang tahun: {siswa}")

# Looping dictionary
print("\n--- Semua Data ---")
for key, value in siswa.items():
    print(f"{key} : {value}")