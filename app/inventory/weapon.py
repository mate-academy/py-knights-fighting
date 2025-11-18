class Weapon:
    def __init__(self, weapon: dict) -> None:
        self.name = weapon.get("name", "")
        self.power = weapon.get("power", 0)
