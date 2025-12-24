from app.knights.knights import Character


class Weapon:
    def __init__(self, knight: Character) -> None:
        self.knight = knight

    def use_weapon(self) -> None:
        if self.knight.weapon:
            self.knight.power += self.knight.weapon["power"]
