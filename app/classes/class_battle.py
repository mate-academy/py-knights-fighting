from app.classes.class_knight import Knight


class Battle:
    @staticmethod
    def knights_battle(knight_one: Knight, knight_two: Knight) -> str:
        knight_one.prepare_for_battle()
        knight_two.prepare_for_battle()
        knight_one.hp -= knight_two.power - knight_one.protection
        knight_two.hp -= knight_one.power - knight_two.protection

        if knight_one.hp <= 0:
            knight_one.hp = 0

        if knight_two.hp <= 0:
            knight_two.hp = 0
