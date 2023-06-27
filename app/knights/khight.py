from app.knights.armour import Armour
from app.knights.potion import Potion
from app.knights.weapon import Weapon


class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: list[Armour],
            weapon: Weapon,
            potion: Potion
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0

    def apply_armour(self) -> None:
        for armour_item in self.armour:
            self.protection += armour_item.protection

    def apply_weapon(self) -> None:
        self.power += self.weapon.power

    def apply_potion(self) -> None:
        if self.potion:
            for key, value in self.potion.effect.items():
                if key == "power":
                    self.power += value
                if key == "hp":
                    self.hp += value
                if key == "protection":
                    self.protection += value
