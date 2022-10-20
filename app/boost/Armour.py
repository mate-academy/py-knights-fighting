class Armour:

    def __init__(self, armour: list) -> None:
        self.armour = armour

    def apply_armour(self, knight: callable) -> None:
        if len(self.armour) > 0:
            for protect in self.armour:
                knight.protection += protect["protection"]
