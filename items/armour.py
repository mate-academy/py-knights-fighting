class Armour:
    armour = {}

    def __init__(self, armour: int, owner: str) -> None:
        self.owner = owner
        self.protection = armour

        Armour.armour[owner] = self
