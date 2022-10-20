class Weapon:

    def __init__(self, weapon: dict) -> None:
        self.power = weapon["power"]

    def apply_weapon(self, knight: callable) -> None:
        knight.power += self.power
