class Armour:
    def __init__(self, armour: list) -> None:
        self.armour = armour

    def apply_armour(self, knight: callable) -> None:
        """apply armour"""
        if len(self.armour) > 0:
            for param in self.armour:
                knight.protection += param["protection"]
