from app.koc.knight import Knight


class Effect:
    def __init__(self
                 , power: int = 0
                 , hp: int = 0
                 , protection: int = 0) -> None:
        self.power = power
        self.hp = hp
        self.protection = protection

    def apply(self, knight: Knight) -> None:
        knight.hp += self.hp
        knight.protection += self.protection
        knight.power += self.power
