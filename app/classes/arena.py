from app.classes.knights import Knight


class Arena:

    fighting_result = {}

    @classmethod
    def fight_in_arena(cls, knight1: Knight, knight2: Knight) -> None:
        knight1.hp -= knight2.power
        if knight1.hp <= 0:
            knight1.hp = 0
        cls.fighting_result[knight1.name] = knight1.hp
        knight2.hp -= knight1.power
        if knight2.hp <= 0:
            knight2.hp = 0
        cls.fighting_result[knight2.name] = knight2.hp
