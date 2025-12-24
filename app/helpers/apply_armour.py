from app.knights.knights import Character


class Armour:
    def __init__(self, knight: Character) -> None:
        self.knight = knight

    def use_armour(self) -> None:
        if len(self.knight.armour) > 0:
            for armour_part in self.knight.armour:
                self.knight.protection += armour_part["protection"]
