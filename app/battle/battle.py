from app.before_battle.knight import Knight


class Battle:

    result_dict = {}

    @classmethod
    def fight(cls, first_knight: Knight, second_knight: Knight) -> None:
        first_knight.hp -= second_knight.power
        if first_knight.hp <= 0:
            first_knight.hp = 0
        cls.result_dict[first_knight.name] = first_knight.hp
        second_knight.hp -= first_knight.power
        if second_knight.hp <= 0:
            second_knight.hp = 0
        cls.result_dict[second_knight.name] = second_knight.hp
