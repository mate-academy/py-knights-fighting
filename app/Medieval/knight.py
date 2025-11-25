from app.Medieval.armour import Armour
from app.Medieval.potion import Potion
from app.Medieval.weapon import Weapon


class Knight:

    list_of_knights = []

    def __init__(self, name: str,
                 power: int,
                 hp: int,
                 armour: list[Armour],
                 weapon: Weapon,
                 potion: Potion) -> None:
        self.name = name
        self.power = power + weapon.power
        self.hp = hp
        self.armour = armour
        self.potion = potion
        self.weapon = weapon
        self.protection = 0
        self.apply_armour()
        self.apply_potion()
        self.list_of_knights.append(self)

    def apply_armour(self) -> None:
        if self.armour:
            for armour in self.armour:
                self.protection += armour.protection

    def apply_potion(self) -> None:
        if self.potion:
            effect = self.potion.effect
            if hasattr(effect, "protection"):
                self.protection += effect.protection
            if hasattr(effect, "hp"):
                self.hp += effect.hp
            if hasattr(effect, "power"):
                self.power += effect.power

    def __str__(self) -> str:
        return (f"{self.name}, POWER: {self.power}, "
                f"HP: {self.hp}, WEAPON: {self.weapon}, "
                f"ARMOUR: {self.armour_to_string()}")

    def armour_to_string(self) -> str:
        armour_name_list = []
        for armour in self.armour:
            armour_name_list.append(f"{armour.part} - {armour.protection}")
        result = ", ".join(armour_name_list)
        return result
