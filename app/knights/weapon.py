from app.knights.knight import Knight


class Weapon:

    def __init__(self, name: str, power: int) -> None:
        self.name = name
        self.power = power

    def apply_weapon(self, knight: Knight) -> None:
        knight.weapon = Weapon(name=self.name, power=self.power)

    def power_calculation(self, knight: Knight):
        knight.power += self.power
