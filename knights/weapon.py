class Weapon:
    def __init__(self, weapon_config: dict) -> None:
        self.name = weapon_config["name"]
        self.power = weapon_config["power"]
