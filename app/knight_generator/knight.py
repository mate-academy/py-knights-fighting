print("Knight __main__")


class Knight:
    def __init__(self,
                 name: str,
                 power: int,
                 hp: int,
                 armour: list[dict],
                 weapon: dict,
                 potion: dict):
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
