#  TUGAS ANALISIS PRAKTIKUM OOP

## 🔹 Tugas Analisis 1

**Pertanyaan:**
Apa yang terjadi jika `hero1.hp` diubah menjadi 500 lalu dilakukan `print(hero1.hp)`?

**Jawaban:**
Nilai HP hero akan langsung berubah menjadi **500** dan berhasil ditampilkan saat dipanggil dengan `print(hero1.hp)`.

**Penjelasan:**
Karena attribute `hp` pada class `Hero` bersifat **public**, maka nilainya bisa diubah langsung dari luar class tanpa pembatasan. Hal ini menunjukkan bahwa tanpa encapsulation, data object bisa dimodifikasi secara bebas, termasuk ke nilai yang tidak realistis dalam konteks game.

---

## 🔹 Tugas Analisis 2

**Pertanyaan:**
Mengapa parameter `lawan` pada method `serang` harus berupa objek, bukan string?

**Jawaban:**
Karena parameter `lawan` digunakan untuk **mengakses method dan attribute milik object lain**, seperti `lawan.diserang()` dan `lawan.name`.

**Penjelasan:**
Jika hanya menggunakan string nama, maka object tersebut tidak memiliki method atau data lain. Dengan menerima object utuh, interaksi antar hero menjadi nyata dan sesuai konsep OOP, yaitu **object saling berkomunikasi melalui method**.

---

## 🔹 Tugas Analisis 3

### 1. Error yang Muncul

Jika `super().__init__(name, hp, attack_power)` dihapus, maka saat menjalankan `eudora.info()` akan muncul error:

> **AttributeError: 'Mage' object has no attribute 'name'**

### 2. Mengapa Error Terjadi?

Walaupun nilai `"Eudora"` dikirim saat pembuatan object, attribute `name`, `hp`, dan `attack_power` **seharusnya dibuat oleh constructor milik class Hero**.
Karena constructor Hero tidak dipanggil, maka attribute tersebut **tidak pernah dibuat**.

### 3. Peran `super()`

Fungsi `super()` berfungsi untuk:

* Memanggil constructor class Induk
* Menghubungkan data dari class Anak ke class Induk
* Memastikan attribute dasar tetap dimiliki oleh object turunan

Tanpa `super()`, object Mage menjadi tidak lengkap.

---

## 🔹 Tugas Analisis 4

### 1. Percobaan Hacking

**Hasil:**
Nilai HP **tetap muncul**, tidak error.

**Penjelasan:**
Python menggunakan **Name Mangling**, di mana `__hp` diubah menjadi `_HeroEncap__hp`.
Hal ini masih bisa diakses secara teknis, namun **melanggar prinsip encapsulation**.

**Kesimpulan:**
Walaupun bisa, cara ini **tidak dianjurkan** karena merusak keamanan dan keterbacaan kode.

---

### 2. Uji Validasi Setter

Jika validasi dihapus dan dilakukan `hero1.set_hp(-100)`:

**Hasil:**
HP akan menjadi **-100**.

**Penjelasan:**
Tanpa setter yang memvalidasi data, nilai tidak logis dapat masuk ke sistem.
Setter sangat penting untuk menjaga **integritas data**, terutama dalam game agar tidak terjadi bug atau cheating.

---

## 🔹 Tugas Analisis 5

### 1. Melanggar Kontrak Interface

**Error yang muncul:**

> Can't instantiate abstract class Hero with abstract method serang

**Makna Error:**
Class yang mewarisi abstract class **wajib mengimplementasikan semua method abstrak**.

**Konsekuensi:**
Jika method yang dijanjikan di interface tidak dibuat, maka class tersebut **tidak bisa dijadikan object**.

---

### 2. Mengapa GameUnit Tidak Bisa Dibuat Object?

Karena `GameUnit` adalah **abstract class**, ia hanya berfungsi sebagai:

* Cetakan
* Standar struktur
* Kontrak method

Gunanya adalah untuk memastikan semua unit game memiliki perilaku dasar yang sama.

---

## 🔹 Tugas Analisis 6

### 1. Uji Skalabilitas (Healer)

**Hasil:**
Program **berjalan lancar tanpa error**.

**Kesimpulan:**
Polimorfisme memungkinkan penambahan karakter baru **tanpa mengubah kode lama**, sehingga game mudah dikembangkan di masa depan.

---

### 2. Konsistensi Penamaan Method

Jika method `serang` diganti menjadi `tembak_panah`:

**Hasil:**
Program mengalami **AttributeError**.

**Penjelasan:**
Dalam polimorfisme, semua class turunan harus memiliki **nama method yang sama**, agar bisa dipanggil secara seragam melalui parent reference atau looping.
