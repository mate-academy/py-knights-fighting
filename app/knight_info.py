class Weapon:

    def __init__(self, name: str, power: int) -> None:
        self.name = name
        self.power = power


class Knight:

    def __init__(self,
                 name: str,
                 power: int,
                 hp: int,
                 weapon: Weapon,
                 armour: list = None,
                 potion: dict = None) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.weapon = weapon
        if armour is None:
            armour = []
        self.armour = armour
        self.potion = potion
        self.protection = 0

    def prepare_for_battle(self) -> None:
        if self.armour:
            for obj in self.armour:
                self.protection += obj["protection"]

        self.power += self.weapon.power

        if self.potion is not None:
            for attr, value in self.potion["effect"].items():
                if attr == "power":
                    self.power += value
                if attr == "protection":
                    self.protection += value
                if attr == "hp":
                    self.hp += value
