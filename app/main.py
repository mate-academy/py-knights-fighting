from app.battle import Battle


def battle(knightsConfig: dict):
    # BATTLE PREPARATIONS:
    battle1 = Battle()
    knights_list = battle1.battle_preparation(knightsConfig)
    lancelot, arthur, mordred, red_knight = knights_list

    # BATTLE:

    # 1 Lancelot vs Mordred:
    battle1.battle(lancelot, mordred)

    # 2 Arthur vs Red Knight:
    battle1.battle(arthur, red_knight)

    # Return battle results:
    return battle1.battle_info
