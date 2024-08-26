class Armour:
    def __init__(self, armour: dict) -> None:
        self.name = armour["part"]
        self.protection = armour["protection"]
