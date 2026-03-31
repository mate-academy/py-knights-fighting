class Weapon:
    def __init__(self, weapon: dict) -> None:
        self.name = weapon['name']
        self.power = weapon['power']

    def use_weapon(self, knight) -> None:
        knight.power += self.power
