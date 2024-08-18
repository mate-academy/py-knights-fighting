from app.equipments.armour import Armour
from app.equipments.weapon import Weapon
from app.equipments.potion import Potion


class Knight:

    def __init__(self,
                 name: str,
                 power: int,
                 hp: int,
                 armours: list[dict],
                 weapon: dict,
                 potion: dict) -> None:

        self.name = name
        self.power = power
        self.hp = hp
        self.armour = [Armour(armour["part"], armour["protection"])
                       for armour in armours]
        self.weapon = Weapon(weapon["name"], weapon["power"])
        self.potion = Potion(
            potion["name"],
            potion["effect"]) if potion else None

    def apply_armour(self) -> None:
        setattr(self, "protection", sum(armour.protection
                                        for armour in self.armour))

    def apply_weapon(self) -> None:
        self.power += self.weapon.power

    def apply_potion(self) -> None:
        if self.potion is not None:
            for stat, value in self.potion.effect.items():
                setattr(self, stat, getattr(self, stat) + value)
