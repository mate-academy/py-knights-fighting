class Weapon:
    def __init__(self, weapon_dict: dict) -> None:
        self.name: str = weapon_dict["name"]
        self.power: int = weapon_dict["power"]


class ArmourPart:
    def __init__(self, armour_dict: dict) -> None:
        self.part: str = armour_dict["part"]
        self.protection: int = armour_dict["protection"]


class Potion:
    def __init__(self, potion_dict: dict | None) -> None:
        if potion_dict is None:
            self.name: str = "None"
            self.hp_effect: int = 0
            self.power_effect: int = 0
            self.protection_effect: int = 0
        else:
            self.name = potion_dict["name"]
            effects = potion_dict.get("effect", {})
            self.hp_effect = effects.get("hp", 0)
            self.power_effect = effects.get("power", 0)
            self.protection_effect = effects.get("protection", 0)
