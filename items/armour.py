class Armour:
    armours = {}

    def __init__(self, armour: int, owner: str) -> None:
        self.owner = owner
        self.protection = armour

        Armour.armours[owner] = self
