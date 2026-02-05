from abc import ABC, abstractmethod

class Hero:
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power

    def info(self):
        print(f"Hero: {self.name} | HP: {self.hp} | Power: {self.attack_power}")

    def serang(self, lawan):
        print(f"{self.name} menyerang {lawan.name}!")
        lawan.diserang(self.attack_power)

    def diserang(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
        print(f"{self.name} terkena damage {damage}. Sisa HP: {self.hp}")


print("\n=== LATIHAN 1 & 2 ===")
hero1 = Hero("Layla", 100, 15)
hero2 = Hero("Zilong", 120, 20)

hero1.info()
hero2.info()

print("\n--- Pertarungan Dimulai ---")
hero1.serang(hero2)
hero2.serang(hero1)

class Mage(Hero):
    def __init__(self, name, hp, attack_power, mana):
        super().__init__(name, hp, attack_power)
        self.mana = mana

    def info(self):
        print(f"{self.name} [Mage] | HP: {self.hp} | Mana: {self.mana}")

    def skill_fireball(self, lawan):
        if self.mana >= 20:
            print(f"{self.name} menggunakan Fireball ke {lawan.name}!")
            self.mana -= 20
            lawan.diserang(self.attack_power * 2)
        else:
            print("Mana tidak cukup!")


print("\n=== LATIHAN 3 (Inheritance) ===")
eudora = Mage("Eudora", 80, 30, 100)
balmond = Hero("Balmond", 200, 10)

eudora.info()
eudora.serang(balmond)
eudora.skill_fireball(balmond)

class HeroEncap:
    def __init__(self, nama, hp_awal):
        self.nama = nama
        self.__hp = hp_awal  # private

    def get_hp(self):
        return self.__hp

    def set_hp(self, nilai_baru):
        if nilai_baru < 0:
            self.__hp = 0
        elif nilai_baru > 1000:
            print("Cheat terdeteksi! HP dibatasi 1000.")
            self.__hp = 1000
        else:
            self.__hp = nilai_baru

    def diserang(self, damage):
        self.set_hp(self.get_hp() - damage)
        print(f"{self.nama} terkena damage {damage}. Sisa HP: {self.get_hp()}")


print("\n=== LATIHAN 4 (Encapsulation) ===")
hero_encap = HeroEncap("Layla", 100)
hero_encap.set_hp(-50)
print("HP sekarang:", hero_encap.get_hp())

class GameUnit(ABC):

    @abstractmethod
    def serang(self, target):
        pass

    @abstractmethod
    def info(self):
        pass


class HeroUnit(GameUnit):
    def __init__(self, nama):
        self.nama = nama

    def serang(self, target):
        print(f"Hero {self.nama} menebas {target}!")

    def info(self):
        print(f"Saya adalah Hero: {self.nama}")


class Monster(GameUnit):
    def __init__(self, jenis):
        self.jenis = jenis

    def serang(self, target):
        print(f"Monster {self.jenis} menggigit {target}!")

    def info(self):
        print(f"Saya adalah Monster: {self.jenis}")


print("\n=== LATIHAN 5 (Abstract & Interface) ===")
h = HeroUnit("Alucard")
m = Monster("Serigala")

h.info()
m.info()
h.serang("Monster")
m.serang("Hero")

class HeroPoly:
    def __init__(self, nama):
        self.nama = nama

    def serang(self):
        print("Hero menyerang.")


class MagePoly(HeroPoly):
    def serang(self):
        print(f"{self.nama} (Mage) menembakkan Bola Api!")


class ArcherPoly(HeroPoly):
    def serang(self):
        print(f"{self.nama} (Archer) memanah dari jauh!")


class FighterPoly(HeroPoly):
    def serang(self):
        print(f"{self.nama} (Fighter) menyerang dengan pedang!")


print("\n=== LATIHAN 6 (Polymorphism) ===")
pasukan = [
    MagePoly("Eudora"),
    ArcherPoly("Miya"),
    FighterPoly("Zilong"),
    MagePoly("Gord")
]

print("--- PERANG DIMULAI ---")
for pahlawan in pasukan:
    pahlawan.serang()