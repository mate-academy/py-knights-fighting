from app.contestants.knight import Knight


class Weapon:
    def __init__(self, weapon_power: int) -> None:
        self.weapon_power = weapon_power

    # apply weapon
    def apply_weapon(self, knight: Knight) -> None:
        knight.power += self.weapon_power
