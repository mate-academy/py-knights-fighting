class Knight:
    def __init__(
        self,
        name: str,
        power: int,
        hp: int,
        armour: int,
        weapon: int,
        potion: list,
    ) -> None:
        self.name = name
        self.power = power
        self.armour = armour
        self.hp = hp
        self.weapon = weapon
        self.potion = potion

    def __str__(self) -> str:
        return (
            f"{self.name}, "
            f"{self.power}, "
            f"{self.armour}, "
            f"{self.hp}, "
            f"{self.weapon}, "
            f"{self.potion}."
        )
