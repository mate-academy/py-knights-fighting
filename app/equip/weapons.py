class Weapon:
    def __init__(self, weapon_data: dict) -> None:
        self.name = weapon_data["name"]
        self.power = weapon_data["power"]
