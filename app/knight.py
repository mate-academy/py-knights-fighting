from __future__ import annotations
from app.items import Armour, Potion, Weapon


class Knight:
    def __init__(self, knight_config: dict) -> None:
        self.name = knight_config["name"]
        self.power = knight_config["power"]
        self.hp = knight_config["hp"]
        self.protection = 0
        if not knight_config["armour"]:
            self.armours = None
        else:
            self.armours = [Armour(item) for item in knight_config["armour"]]
        if knight_config["potion"] is None:
            self.potion = None
        else:
            self.potion = Potion(knight_config["potion"])
        self.weapon = Weapon(knight_config["weapon"])

    def wear_armour(self) -> None:
        if self.armours is not None:
            for armour in self.armours:
                self.protection += armour.protection
                print(f"{self.name} wear {armour.part}"
                      f" and get {armour.protection} protection")

    def drink_potion(self) -> None:
        if self.potion is not None:
            print(f"{self.name} drink {self.potion.name} and get:")
            if self.potion.hp_effect is not None:
                self.hp += self.potion.hp_effect
                print(f"{self.potion.hp_effect} HP")
            if self.potion.power_effect is not None:
                self.power += self.potion.power_effect
                print(f"{self.potion.power_effect} power")
            if self.potion.protection_effect is not None:
                self.protection += self.potion.protection_effect
                print(f"{self.potion.protection_effect} protection.")

    def wear_weapon(self) -> None:
        self.power += self.weapon.power
        print(f"{self.name} wear {self.weapon.name}"
              f" and get {self.weapon.power} power")

    def prepare_to_battle(self) -> None:
        self.wear_armour()
        self.drink_potion()
        self.wear_weapon()

    @staticmethod
    def duel(knight1: Knight, knight2: Knight) -> dict:
        knight1.prepare_to_battle()
        knight2.prepare_to_battle()
        print(f"{knight1.name} has:"
              f" {knight1.hp}HP,"
              f" {knight1.protection} protection,"
              f" {knight1.power} power")
        print(f"{knight2.name} has:"
              f" {knight2.hp}HP,"
              f" {knight2.protection} protection,"
              f" {knight2.power} power")
        knight1_hit = knight1.power - knight2.protection
        knight2_hit = knight2.power - knight1.protection
        knight2.hp -= knight1_hit
        knight1.hp -= knight2_hit
        print(f"{knight1.name} hit {knight2.name} HP by {knight1_hit} damage")
        print(f"{knight2.name} hit {knight1.name} HP by {knight2_hit} damage")
        if knight1.hp < 0:
            knight1.hp = 0
        if knight2.hp < 0:
            knight2.hp = 0
        return {knight1.name: knight1.hp, knight2.name: knight2.hp}
