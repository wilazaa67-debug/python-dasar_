class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim
    def perkenalan(self):
        return f"Halo, saya {self.nama} NIM {self.nim}"
mhs = Mahasiswa("Wili", "123")
print(mhs.perkenalan())