class Knight:
    """
    Create Knight class instance and store its attributes.
    """
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            weapon: dict,
            armour: list,
            potion: dict
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.weapon = weapon
        self.armour = armour
        self.potion = potion
        self.protection = None

    def __repr__(self) -> str:
        return (f"{self.__class__.__name__} class, "
                f"name: {self.name}, "
                f"power: {self.power}, "
                f"hp: {self.hp}, "
                f"weapon: {self.weapon}, "
                f"armour: {self.armour},"
                f"potion: {self.potion},"
                f"protection: {self.protection}")
