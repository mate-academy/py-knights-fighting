from app.armour.armour import Armour
from app.potion.potion import Potion
from app.weapon.weapon import Weapon


class Knight:
    def __init__(self, name: str, power: int,
                 hp: int, weapon: dict,
                 armour: list,
                 potion: dict):
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = Armour.get_total_armour(armour)
        self.weapon = Weapon.get_weapon_cls(weapon)
        self.potion = Potion.get_potion_cls(potion)

    def __repr__(self):
        return self.name

    # create Knight instance
    @classmethod
    def get_knight_cls(cls, knight: dict) -> "Knight":
        return cls(
            name=knight["name"],
            power=knight["power"],
            hp=knight["hp"],
            armour=knight["armour"],
            weapon=knight["weapon"],
            potion=knight["potion"]
        )

    # knight's statistics before the battle
    def get_knight_stats(self):
        self.total_hp = self.hp + self.potion.hp
        self.total_power = self.power + self.potion.power + self.weapon.power
        self.total_armour = self.armour + self.potion.protection

    # battle between two knights
    @classmethod
    def battle_between(cls, first_knight, second_knight):
        first_knight.get_knight_stats()
        second_knight.get_knight_stats()

        first_defense = second_knight.total_power - first_knight.total_armour
        second_defense = first_knight.total_power - second_knight.total_armour

        first_knight.health = first_knight.total_hp - first_defense
        second_knight.health = second_knight.total_hp - second_defense

        if first_knight.health < 0:
            first_knight.health = 0

        if second_knight.health < 0:
            second_knight.health = 0

    # get dictionary with knights
    @staticmethod
    def convert(knights: dict) -> dict:
        return {
            knight: Knight.get_knight_cls(features)
            for knight, features in knights.items()
        }
