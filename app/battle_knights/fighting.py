from app.creation_knights.knights_stats import Knight


class Battle:

    @staticmethod
    def combat(warrior_1: Knight, warrior_2: Knight) -> None:
        warrior_1.hp -= warrior_2.power - warrior_1.protection
        warrior_2.hp -= warrior_1.power - warrior_2.protection

    @staticmethod
    def check_death(warriors: dict) -> None:
        for characteristics in warriors.values():
            if characteristics.hp <= 0:
                characteristics.hp = 0
