from app.battle.battle import Battle
from app.knights.battle_preparation import Preparation


def battle(knightsConfig):
    battle_result = {}

    # BATTLE PREPARATIONS:

    preparation = Preparation(knightsConfig)
    preparation = preparation.battle_preparation()

    # -------------------------------------------------------------------------------
    # BATTLE:

    # 1 Lancelot vs Mordred:
    battle_1 = Battle(preparation)
    battle_1_res = battle_1.versus("Lancelot", "Mordred")

    # 2 Arthur vs Red Knight:
    battle_2 = Battle(preparation)
    battle_2_res = battle_2.versus("Artur", "Red Knight")

    # Return battle results:
    battle_result.update(battle_1_res)
    battle_result.update(battle_2_res)
    return battle_result
