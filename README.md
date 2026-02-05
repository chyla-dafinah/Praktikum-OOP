# 📘 LAPORAN HASIL PRAKTIKUM OOP PYTHON
---
## 🔹 Praktikum 1 & 2 – Class dan Object

### Tujuan

Memahami konsep **class**, **object**, **attribute**, dan **method** dalam Python.

### Penjelasan

Pada praktikum ini dibuat class `Hero` yang memiliki:

* **Attribute:** `name`, `hp`, `attack_power`
* **Method:** `info()`, `serang()`, dan `diserang()`

Dua object dibuat dari class Hero, yaitu `Layla` dan `Zilong`, lalu dilakukan simulasi serangan antar hero.

### Output Program

* Menampilkan informasi hero
* Hero saling menyerang
* HP lawan berkurang sesuai attack power

### Analisis

Konsep OOP dasar diterapkan dengan baik karena:

* Object memiliki data dan perilaku sendiri
* Interaksi antar object terjadi melalui method

---

## 🔹 Praktikum 3 – Inheritance (Pewarisan)

### Tujuan

Memahami konsep **inheritance**, yaitu class turunan dari class induk.

### Penjelasan

Class `Mage` dibuat sebagai turunan dari `Hero`.
Class ini menambahkan:

* Attribute `mana`
* Method khusus `skill_fireball()`

Mage tetap bisa menggunakan method milik Hero seperti `serang()`.

### Output Program

* Mage menampilkan info HP dan Mana
* Mage menyerang hero lain
* Mage menggunakan skill Fireball jika mana cukup

### Analisis

Inheritance membuat kode lebih efisien karena:

* Tidak perlu menulis ulang atribut dan method Hero
* Class Mage menjadi lebih spesifik dengan kemampuan tambahan

---

## 🔹 Praktikum 4 – Encapsulation

### Tujuan

Memahami konsep **encapsulation** (pembatasan akses data).

### Penjelasan

Class `HeroEncap` menggunakan attribute private `__hp`.
Akses HP hanya bisa melalui:

* `get_hp()`
* `set_hp()`

Nilai HP dibatasi agar tidak negatif dan tidak melebihi 1000.

### Output Program

* HP tidak bisa diatur sembarangan
* Jika HP negatif, otomatis menjadi 0

### Analisis

Encapsulation menjaga data tetap aman dan valid, serta mencegah manipulasi langsung dari luar class.

---

## 🔹 Praktikum 5 – Abstract Class & Interface

### Tujuan

Memahami konsep **abstract class** menggunakan modul `abc`.

### Penjelasan

Class `GameUnit` dibuat sebagai abstract class dengan method:

* `serang()`
* `info()`

Class `HeroUnit` dan `Monster` wajib mengimplementasikan method tersebut.

### Output Program

* Hero dan Monster menampilkan identitas
* Hero dan Monster memiliki cara menyerang berbeda

### Analisis

Abstract class memastikan setiap class turunan memiliki struktur method yang sama, sehingga program lebih terorganisir.

---

## 🔹 Praktikum 6 – Polymorphism

### Tujuan

Memahami konsep **polymorphism**, yaitu method yang sama tetapi perilaku berbeda.

### Penjelasan

Beberapa class (`MagePoly`, `ArcherPoly`, `FighterPoly`) memiliki method `serang()` dengan aksi berbeda.

Semua object disimpan dalam satu list dan dipanggil menggunakan satu method yang sama.

### Output Program

* Setiap hero menyerang dengan gaya berbeda
* Method `serang()` menghasilkan output sesuai tipe hero

### Analisis

Polymorphism membuat program fleksibel dan mudah dikembangkan tanpa mengubah struktur utama.

---

## ✅ Kesimpulan

Dari praktikum 1–6 dapat disimpulkan bahwa:

* OOP mempermudah pengelolaan kode
* Setiap konsep OOP saling berkaitan
* Program menjadi lebih rapi, aman, dan scalable
