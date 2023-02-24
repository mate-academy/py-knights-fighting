from knight import Knight


class Armour:
    def __init__(self, part: str, protection: int) -> None:
        self.part = part
        self.protection = protection

    def wear_armour(self, knight: Knight) -> None:
        knight.protection += self.protection
        print(f"{knight.name} wear {self.part} and get {self.protection} protection")


class Potion:
    def __init__(self, name: str, effect: int) -> None:
        self.name = name
        self.hp_effect = effect["hp"]
        self.power_effect = effect["power"]
        self.protection_effect = effect["protection"]

    def drink_potion(self, knight: Knight) -> None:
        knight.hp += self.hp_effect
        knight.power += self.power_effect
        knight.protection += self.protection_effect
        print(f"{knight.name} drink {self.name} and get:"
              f" {self.protection_effect} protection")


class Weapon:
    def __init__(self, name: str, power: int) -> None:
        self.name = name
        self.power = power

    def wear_weapon(self, knight: Knight) -> None:
        knight.power += self.power
        print(f"{knight.name} wear {self.name} and get {self.power} power")