from app.battle_results import BattleResults
from app.knights_data import KNIGHTS
from app.preparation import Preparation


def battle(knights):
    # BATTLE PREPARATIONS:

    list_of_knights = []

    # Lancelot's preparations
    for name in knights:
        knights[name]["protection"] = 0
        knight = Preparation(knights[name])
        knight.armour()
        knight.weapon()
        knight = knight.potion()
        list_of_knights.append(knight)

    # -------------------------------------------------------------------------------
    # BATTLE:

    list_of_knights[0].hp, list_of_knights[2].hp = BattleResults(
        list_of_knights[0],
        list_of_knights[2]
    ).battle_results()
    list_of_knights[1].hp, list_of_knights[3].hp = BattleResults(
        list_of_knights[1],
        list_of_knights[3]
    ).battle_results()

    # Return battle results:
    return {
        list_of_knights[0].name: list_of_knights[0].hp,
        list_of_knights[1].name: list_of_knights[1].hp,
        list_of_knights[2].name: list_of_knights[2].hp,
        list_of_knights[3].name: list_of_knights[3].hp,
    }


print(battle(KNIGHTS))
