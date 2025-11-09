from app.knights.knights import Character


class Weapon:
    def __init__(self, knight: Character):
        self.knight = knight

    def use_weapon(self):
        # self.knight: Knight["power"] += self.knight: Knight["weapon"]["power"]
        if self.knight.weapon:
            self.knight.power += self.knight.weapon["power"]