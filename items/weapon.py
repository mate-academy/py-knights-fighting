class Weapon:
    list_of_weapons = []

    def __init__(self, weapon: dict, owner: str) -> None:
        self.owner = owner
        self.name = weapon["name"]
        self.power = weapon["power"]

        Weapon.list_of_weapons.append(self)
