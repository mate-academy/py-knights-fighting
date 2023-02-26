from app.knights.knight import Knight


class Armour:

    def __init__(self, name: str, protection: int) -> None:
        self.name = name
        self.protection = protection

    def check_armour(self, knight: Knight) -> None:
        knight.armour = Armour(name=self.name, protection=self.protection)

    def update_protection(self, knight: Knight, effect: int) -> None:
        if knight.armour is self:
            self.protection += effect
