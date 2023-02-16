from app.before_battle.knight import Knight


class Battle:

    result_dict = {}

    @classmethod
    def fight(cls, first_knight: Knight, second_knight: Knight) -> None:
        def check_hp(cls: Knight) -> int:
            if cls.hp <= 0:
                cls.hp = 0
                return cls.hp
        first_knight.hp -= second_knight.power
        second_knight.hp -= first_knight.power
        check_hp(first_knight)
        check_hp(second_knight)
        cls.result_dict[first_knight.name] = first_knight.hp
        cls.result_dict[second_knight.name] = second_knight.hp
