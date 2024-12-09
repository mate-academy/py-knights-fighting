from __future__ import annotations

from app.armour.armour import Armour
from app.weapons.weapon import Weapon
from app.potion.potion import Potion


class Knight:
    def __init__(self, name: str, power: int, hp: int) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = 0
        self.armour_set = []
        self.weapon = None

    def dress_up(self, armour: Armour) -> None:
        self.armour_set.append(armour)
        self.protection += armour.protection

    def get_weapon(self, weapon: Weapon) -> None:
        self.weapon = weapon
        self.power += weapon.power

    def drink_potion(self, potion: Potion) -> None:
        if potion:
            if "power" in potion.effects:
                self.power += potion.effects["power"]
            if "protection" in potion.effects:
                self.protection += potion.effects["protection"]
            if "hp" in potion.effects:
                self.hp += potion.effects["hp"]
        return

    def hit(self, enemy: Knight) -> None:
        enemy.hp -= self.power - enemy.protection
        if enemy.hp < 0:
            enemy.hp = 0

    @classmethod
    def prepare_knight(cls, knight_config_name: str, config: dict) -> Knight:
        knight = cls(
            config[knight_config_name]["name"],
            config[knight_config_name]["power"],
            config[knight_config_name]["hp"]
        )

        knight_armour_set = config[knight_config_name]["armour"]
        knight_weapon = Weapon.create_weapon(
            config[knight_config_name]["weapon"]
        )
        knight_potion = Potion.create_potion(
            config[knight_config_name]["potion"]
        )

        for armour in knight_armour_set:
            knight.dress_up(
                Armour(
                    armour["part"], armour["protection"]
                )
            )

            print(f"{knight.name} is putting on {armour["part"]}")

        knight.get_weapon(knight_weapon)
        print(f"{knight.name} is gonna fight with {knight_weapon.name}!")

        if knight_potion:
            knight.drink_potion(knight_potion)
            print(f"{knight.name} just drank {knight_potion.name}!")

        return knight

    def __str__(self) -> str:
        return (
            f"Name: {self.name}\n"
            f"Protection: {self.protection}\n"
            f"Health: {self.hp}\n"
            f"Weapon: {self.weapon}\n"
            f"Armour: {self.armour_set}"
        )
