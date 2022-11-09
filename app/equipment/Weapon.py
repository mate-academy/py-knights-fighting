class Weapon:
    def __init__(self, weapon: dict) -> None:
        self.name = weapon["name"]
        self.power = weapon["power"]

    def apply_weapon(self, knight: callable) -> None:
        knight.power += self.power
