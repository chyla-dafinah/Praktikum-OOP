from abc import ABC, abstractmethod
class BarangElektronik(ABC):
    def __init__(self, nama, harga_dasar):
        self.nama = nama
        self.__stok = 0
        self.__harga_dasar = harga_dasar

    # ENCAPSULATION
    def get_stok(self):
        return self.__stok

    def tambah_stok(self, jumlah):
        if jumlah < 0:
            print(f"Gagal update stok {self.nama}! Stok tidak boleh negatif ({jumlah}).")
        else:
            self.__stok += jumlah
            print(f"Berhasil menambahkan stok {self.nama}: {jumlah} unit.")

    def get_harga_dasar(self):
        return self.__harga_dasar

    # ABSTRACTION
    @abstractmethod
    def tampilkan_detail(self):
        pass

    @abstractmethod
    def hitung_harga_total(self, jumlah):
        pass

class Laptop(BarangElektronik):
    def __init__(self, nama, harga_dasar, processor):
        super().__init__(nama, harga_dasar)
        self.processor = processor

    def tampilkan_detail(self):
        pajak = self.get_harga_dasar() * 0.10
        print(f"[LAPTOP] {self.nama} | Proc: {self.processor}")
        print(f" Harga Dasar: Rp {self.get_harga_dasar():,} | Pajak(10%): Rp {int(pajak):,}")

    def hitung_harga_total(self, jumlah):
        pajak = self.get_harga_dasar() * 0.10
        return (self.get_harga_dasar() + pajak) * jumlah

class Smartphone(BarangElektronik):
    def __init__(self, nama, harga_dasar, kamera):
        super().__init__(nama, harga_dasar)
        self.kamera = kamera

    def tampilkan_detail(self):
        pajak = self.get_harga_dasar() * 0.05
        print(f"[SMARTPHONE] {self.nama} | Cam: {self.kamera}")
        print(f" Harga Dasar: Rp {self.get_harga_dasar():,} | Pajak(5%): Rp {int(pajak):,}")

    def hitung_harga_total(self, jumlah):
        pajak = self.get_harga_dasar() * 0.05
        return (self.get_harga_dasar() + pajak) * jumlah

def proses_transaksi(daftar_barang):
    print("\n--- STRUK TRANSAKSI ---")
    total = 0
    for i, (barang, jumlah) in enumerate(daftar_barang, start=1):
        barang.tampilkan_detail()
        subtotal = barang.hitung_harga_total(jumlah)
        print(f" Beli: {jumlah} unit | Subtotal: Rp {int(subtotal):,}\n")
        total += subtotal

    print("----------------------------------------")
    print(f"TOTAL TAGIHAN: Rp {int(total):,}")
    print("----------------------------------------")

print("--- SETUP DATA ---")

laptop1 = Laptop("ROG Zephyrus", 20_000_000, "Ryzen 9")
hp1 = Smartphone("iPhone 13", 15_000_000, "12MP")

laptop1.tambah_stok(10)
hp1.tambah_stok(-5)
hp1.tambah_stok(20)

keranjang = [
    (laptop1, 2),
    (hp1, 1)
]

proses_transaksi(keranjang)