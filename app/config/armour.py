class Armour:
    def __init__(self, armour: dict = None) -> None:
        if armour is not None:
            self.part = armour["part"]
            self.protection = armour["protection"]
        else:
            self.part = None
            self.protection = None
