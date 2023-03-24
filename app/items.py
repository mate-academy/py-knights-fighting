class Armour:
    def __init__(self, armour_conf: dict) -> None:
        self.part = armour_conf["part"]
        self.protection = armour_conf["protection"]


class Potion:
    def __init__(self, potion_conf: dict) -> None:
        self.name = potion_conf["name"]
        self.protection_effect = potion_conf["effect"].get("protection")
        self.power_effect = potion_conf["effect"].get("power")
        self.hp_effect = potion_conf["effect"].get("hp")


class Weapon:
    def __init__(self, weapon_conf: dict) -> None:
        self.name = weapon_conf["name"]
        self.power = weapon_conf["power"]
