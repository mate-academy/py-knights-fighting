class Knight:

    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: list = None,
            weapon: dict = None,
            potion: int = None
    ) -> None:

        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0
