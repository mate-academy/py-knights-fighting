class Knight:
    def __init__(
        self,
        name: str,
        power: int,
        hp: int,
        armour: list[dict],
        weapon: dict | None = None,
        potion: dict | None = None,
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
