from app.knights.knights import Character


class Armour:
    def __init__(self, knight: Character) -> None:
        self.knight = knight

    def use_armour(self) -> None:
        if len(self.knight.armour) > 0:
            for armo_unit in self.knight.armour:
                self.knight.protection += armo_unit["protection"]
