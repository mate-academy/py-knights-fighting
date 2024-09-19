class Knight:
    def __init__(self, name: str, power: int, hp: int,
                 armour: list = [], weapon: dict = {},
                 potion: dict = None) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion

    def __repr__(self) -> str:
        return  str(self.__dict__)