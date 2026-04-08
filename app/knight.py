from .equipment import Armour, Weapon, Potion


class Knight:
    def __init__(self, name: str, power: int = 0, hp: int = 0) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = 0
        self.armour = []
        self.weapon = None
        self.potion = None

    def equip_armour(self, armour: Armour) -> None:
        self.armour.append(armour)
        self.protection += armour.protection

    def equip_weapon(self, weapon: Weapon) -> None:
        self.weapon = weapon
        self.power += weapon.power

    def drink_potion(self, potion: Potion) -> None:
        self.potion = potion
        for stat, value in potion.effect.items():
            if stat == "hp":
                self.hp += value
            elif stat == "power":
                self.power += value
            elif stat == "protection":
                self.protection += value
