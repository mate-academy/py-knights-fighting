class Armour:
    def __init__(self, armor_info: dict) -> None:
        self.part = armor_info["part"]
        self.protection = armor_info["protection"]


class Weapon:
    def __init__(self, weapon_info: dict) -> None:
        self.name = weapon_info["name"]
        self.power = weapon_info["power"]


class Potion:
    def __init__(self, potion_info: dict) -> None:
        self.name = potion_info["name"]
        self.effect = potion_info["effect"]
