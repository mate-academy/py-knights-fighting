from app.units.knight import Knight


class Battle:
    @staticmethod
    def fight(power: int, protection: int) -> int:
        return power - protection

    @staticmethod
    def check_hp_results(knight: Knight) -> int:
        return 0 if knight.hp <= 0 else knight.hp
