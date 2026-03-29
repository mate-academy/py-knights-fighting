from app.Knight import Knight
from app.config import knights, battle_table


def battle(config: dict) -> dict:
    result = {}
    for first_name, second_name in battle_table.items():
        knight1 = Knight(config[first_name])
        knight2 = Knight(config[second_name])
        knight1.arm_the_warrior()
        knight2.arm_the_warrior()
        hp_1 = knight1.hp - (knight2.power - knight1.protection)
        hp_2 = knight2.hp - (knight1.power - knight2.protection)
        result[knight1.name] = hp_1 if hp_1 > 0 else 0
        result[knight2.name] = hp_2 if hp_2 > 0 else 0
    return result


print(battle(knights))
