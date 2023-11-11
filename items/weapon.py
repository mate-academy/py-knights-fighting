class Weapon:
    weapons = {}

    def __init__(self, weapon: dict, owner: str) -> None:
        self.owner = owner
        self.power = weapon["power"]

        Weapon.weapons[weapon["name"]] = self
