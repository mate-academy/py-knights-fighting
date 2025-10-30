from app.knights_pack.knights_data import Knight


class PrepareForBattle:

    @staticmethod
    def give_armor(knight: Knight, hp: int = 0) -> None:
        knight.knight_hp += hp

    @staticmethod
    def give_protection(knight: Knight, protection: int = 0) -> None:
        knight.knight_protection += protection

    @staticmethod
    def give_power(knight: Knight, power: int = 0) -> None:
        knight.knight_power += power
