from app.contestants.knight import Knight


class Armour:
    def __init__(self, armour: list) -> None:
        self.armour = armour

    # apply armour
    def apply_armour(self, knight: Knight) -> None:
        knight.protection = 0
        for part in self.armour:
            knight.protection += part["protection"]
