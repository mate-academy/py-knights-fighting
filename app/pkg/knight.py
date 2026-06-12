from app.pkg.armour import Armour
from app.pkg.potion import Potion
from app.pkg.weapon import Weapon


class Knight:

    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = 0
        self.weapon = None
        self.armour = []
        self.potion = None

    def apply_weapon(self, weapon: Weapon) -> None:
        self.power += weapon.power

    def apply_armour(self, armour_list: list[Armour]) -> None:
        for armour in armour_list:
            self.protection += armour.protection

    def apply_potion_effect(self, potion: Potion) -> None:
        if self.potion is not None:
            for key, value in potion.effect.items():
                if key == "hp":
                    self.hp += value
                if key == "power":
                    self.power += value
                if key == "protection":
                    self.protection += value
