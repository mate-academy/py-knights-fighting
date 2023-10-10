class Weapon:
    def __init__(self, weapon_info: dict) -> None:
        self.name = weapon_info["name"]
        self.power = weapon_info["power"]
