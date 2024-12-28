from app.battle import BattleKnight
from app.config import knights_list


def find_knight_by_name(knights, name):
    for knight in knights:
        if knight.name == name:
            return knight
    raise ValueError(f"Knight with name '{name}' not found.")


def battle(knights: list) -> dict:
    battle1 = BattleKnight(knights_list)

    battle1.battle_preparation()

    lancelot = find_knight_by_name(knights_list, "Lancelot")
    mordred = find_knight_by_name(knights_list, "Mordred")
    arthur = find_knight_by_name(knights_list, "Arthur")
    red_knight = find_knight_by_name(knights_list, "Red Knight")

    battle1.battle_process(lancelot, mordred)
    battle1.battle_process(arthur, red_knight)

    return battle1.show_battle_results()


print(battle(knights_list))