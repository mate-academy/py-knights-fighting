class Armour:
    def __init__(self, armour: dict) -> None:
        self.part_name: str = armour["part"]
        self.protection: int = armour["protection"]


class Weapon:
    def __init__(self, weapon: dict) -> None:
        self.name: str = weapon["name"]
        self.power: int = weapon["power"]


class Potion:
    def __init__(self, potion: dict) -> None:
        self.name: str = potion["name"]
        self.effect: dict = potion["effect"]
