from app.knights_dict.config import KNIGHTS, battle_table
from app.knights_dict.knights import Knight


def battle(config: dict) -> dict:
    result = {}
    for first_name, second_name in battle_table.items():
        knight_1 = Knight(config[first_name])
        knight_2 = Knight(config[second_name])
        knight_1.arm_the_warrior()
        knight_2.arm_the_warrior()
        hp_1 = knight_1.hp - (knight_2.power - knight_1.protection)
        hp_2 = knight_2.hp - (knight_1.power - knight_2.protection)
        result[knight_1.name] = hp_1 if hp_1 > 0 else 0
        result[knight_2.name] = hp_2 if hp_2 > 0 else 0
    return result


print(battle(KNIGHTS))
