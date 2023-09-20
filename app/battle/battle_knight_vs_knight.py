from app.knight_config.config import Knight


class Battle:
    @staticmethod
    def battle(first_knight: Knight, other: Knight) -> tuple:
        first_knight.hp -= other.power - first_knight.protection
        other.hp -= first_knight.power - other.protection
        return first_knight, other
