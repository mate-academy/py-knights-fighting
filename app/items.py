class Armour:
    def __init__(self, armour_conf: dict) -> None:
        self.part = armour_conf["part"]
        self.protection = armour_conf["protection"]


class Potion:
    def __init__(self, potion_conf: dict) -> None:
        self.name = potion_conf["name"]
        self.protection_effect = None
        self.power_effect = None
        self.hp_effect = None
        for key, value in potion_conf["effect"].items():
            if key == "hp":
                self.hp_effect = value
            if key == "power":
                self.power_effect = value
            if key == "protection":
                self.protection_effect = value


class Weapon:
    def __init__(self, weapon_conf: dict) -> None:
        self.name = weapon_conf["name"]
        self.power = weapon_conf["power"]
