from typing import List
from app.battle import BattleKnight
from app.config import knights_list
from app.knights import Knight


def find_knight_by_name(knights: List[Knight], name: str) -> Knight:
    for knight in knights:
        if knight.name == name:
            return knight
    raise ValueError(f"Knight with name '{name}' not found.")


def battle(knights: List[Knight]) -> dict:
    battle1 = BattleKnight(knights)

    battle1.battle_preparation()

    lancelot = find_knight_by_name(knights, "Lancelot")
    mordred = find_knight_by_name(knights, "Mordred")
    arthur = find_knight_by_name(knights, "Arthur")
    red_knight = find_knight_by_name(knights, "Red Knight")

    battle1.battle_process(lancelot, mordred)
    battle1.battle_process(arthur, red_knight)

    return battle1.show_battle_results()


print(battle(knights_list))
