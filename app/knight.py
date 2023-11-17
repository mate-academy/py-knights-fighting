from app.equipment.weapon import Weapon
from app.equipment.armour import TotalArmour, ArmourPart
from app.equipment.potion import Potion


class Knight:
    def __init__(self, knight_info: dict) -> None:

        self.name = knight_info.get("name")
        self.power = knight_info.get("power")
        self.hp = knight_info.get("hp")
        self.weapon = self.__create_weapon(knight_info.get("weapon"))
        self.armour = self.__create_armour(knight_info.get("armour"))
        self.potion = self.__create_potion(knight_info.get("potion"))
        self.protection = 0

    def __create_weapon(self, weapon_info: dict) -> Weapon:
        return Weapon(weapon_info)

    def __create_armour(self, armour_info: list) -> TotalArmour:
        armour_parts = [
            ArmourPart(part["part"], part["protection"])
            for part in armour_info
        ]
        return TotalArmour(armour_parts)

    def __create_potion(self, potion_info: dict) -> Potion:
        if potion_info:
            return Potion(potion_info)

    def apply_armour(self) -> None:
        for part in self.armour:
            self.protection += part.protection

    def apply_weapon(self) -> None:
        self.power += self.weapon.power

    def apply_potion(self) -> None:
        if self.potion:
            for stat, value in self.potion.effect.items():
                self.__dict__[stat] += value

    def fight(self, opponent: "Knight") -> None:
        self.hp -= opponent.power - self.protection
        opponent.hp -= self.power - opponent.protection

    def is_alive(self) -> bool:
        if self.hp <= 0:
            self.hp = 0
            return False
        return True
