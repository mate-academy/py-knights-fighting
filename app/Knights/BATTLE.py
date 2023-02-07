from app.Knights.Preparation import PrepareKnight


class Battle:

    @staticmethod
    def fight(first: PrepareKnight, second: PrepareKnight) -> None:
        first.hp -= second.power - first.armour
        second.hp -= first.power - second.armour
        if first.hp <= 0:
            first.hp = 0
        if second.hp <= 0:
            second.hp = 0

    @staticmethod
    def battle_result(fight_dict: dict) -> dict:
        return {name: info.hp for name, info in fight_dict.items()}
