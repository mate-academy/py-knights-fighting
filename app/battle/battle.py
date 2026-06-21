from app.knights.knight import Knight


class Battle:
    @staticmethod
    def begin_battle(first_knight: Knight, second_knight: Knight) -> None:
        first_knight.health -= second_knight.power - first_knight.armour
        second_knight.health -= first_knight.power - second_knight.armour

        # check if someone fell in battle
        if first_knight.health <= 0:
            first_knight.health = 0

        if second_knight.health <= 0:
            second_knight.health = 0

    @staticmethod
    def result_of_battle(*args) -> dict:
        result = {}
        for knight in args:
            result[knight.name] = knight.health

        return result
