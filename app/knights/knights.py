class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            weapon: dict,
            armor: list,
            potion: dict
    ) -> None:
        self.name = name.replace("_", " ")
        self.hp = hp
        self.power = power
        self.weapon = weapon
        self.armor = armor
        self.potion = potion
        self.protection = 0
