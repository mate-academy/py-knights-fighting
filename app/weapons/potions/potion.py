from app.weapons.weapon import Weapon


class Potion(Weapon):
    def __init__(self, name, power=0, protection=0, hp=0):
        super().__init__(name, power)
        self.protection = protection
        self.hp = hp

    def __repr__(self):
        return f"{self.name}"
