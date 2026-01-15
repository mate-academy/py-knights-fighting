from app.knight_config.config import Knight


class Check:
    result_dict = {}

    @staticmethod
    def check_knights(battle_result: tuple[Knight]) -> dict:
        for result in battle_result:
            if result.hp <= 0:
                result.hp = 0
            Check.result_dict[result.name] = result.hp
        return Check.result_dict
