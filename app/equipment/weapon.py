class Weapon:
    def __init__(self, weapon_cfg: dict) -> None:
        self.name = weapon_cfg["name"]
        self.power = weapon_cfg["power"]
