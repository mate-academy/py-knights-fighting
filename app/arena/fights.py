from app.knights.knight import Knight, knights

class Arena:

    @staticmethod
    def arena_fight(knight_one: Knight, knight_two:Knight) -> None:

        knight_one.arm_knight()
        knight_two.arm_knight()

        knight_one.hp -= knight_two.power - knight_two.protection
        knight_two.hp += knight_one.power - knight_two.protection

        if knight_one.hp <= 0:
            knight_one.hp = 0
        if knight_two.hp <= 0:
            knight_two.hp = 0

    @staticmethod
    def get_fight_results() -> dict:

        Arena.arena_fight(knights["lancelot"], knights["mordred"])
        Arena.arena_fight(knights["arthur"], knights["red_knight"])

        return {knight.name: knight.hp for knight in knights.values()}
