from app.knights.knight import Knight


class Arena:

    @staticmethod
    def arena_fight(knight_one: Knight,
                    knight_two: Knight) -> tuple[Knight, Knight] :

        armed_knight_one = knight_one.arm_knight()
        armed_knight_two = knight_two.arm_knight()

        dmg_one = 0
        dmg_two = 0

        if armed_knight_two.power > armed_knight_one.protection:
            dmg_one = armed_knight_two.power - armed_knight_one.protection

        if armed_knight_one.power > armed_knight_two.protection:
            dmg_two = armed_knight_one.power - armed_knight_two.protection

        armed_knight_one.hp -= dmg_one
        armed_knight_two.hp -= dmg_two

        if armed_knight_one.hp <= 0:
            armed_knight_one.hp = 0
        if armed_knight_two.hp <= 0:
            armed_knight_two.hp = 0

        return armed_knight_one, armed_knight_two
