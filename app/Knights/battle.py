from app.Knights.preparation import Knight


class Battle:
    @staticmethod
    def fight(first: Knight, second: Knight) -> None:
        first.hp -= second.power - first.armour
        second.hp -= first.power - second.armour
        if first.hp <= 0:
            first.hp = 0
        if second.hp <= 0:
            second.hp = 0

    @staticmethod
    def battle_result(fight_dict: dict) -> dict:
        return {name: info.hp for name, info in fight_dict.items()}
