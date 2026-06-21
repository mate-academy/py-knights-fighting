from app.knights.knight import Knight


class Weapon:
    @staticmethod
    def apply_weapon(knight: Knight) -> None:
        knight.power += knight.weapon["power"]
