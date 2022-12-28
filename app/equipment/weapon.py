class Weapon:
    def __init__(self, weapon_dict: dict) -> None:
        self.name = weapon_dict["name"]
        self.power = weapon_dict["power"]
