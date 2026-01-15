from app.knight_config.config import Knight


class Weapon:
    @staticmethod
    def weapon_power(knight: Knight) -> Knight:
        knight.power += knight.weapon.get("power")
        return knight.power
