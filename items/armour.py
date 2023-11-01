class Armour:
    list_of_armour = []

    def __init__(self, armour: dict, owner: str) -> None:
        self.owner = owner
        self.part = armour["part"]
        self.protection = armour["protection"]

        Armour.list_of_armour.append(self)
