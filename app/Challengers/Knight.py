class Hero:
    def __init__(self, name: str,
                 power: int,
                 hp: int,
                 armour: int = 0) -> None:

        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
