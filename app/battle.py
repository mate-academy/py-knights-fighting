from participant.knight import Knight


def battle(knights_config: dict) -> dict:
    # BATTLE PREPARATIONS:
    knights = []

    # create knights and apply equipment
    for knight in knights_config.values():
        new_knight = Knight(knight)
        new_knight.apply_all_equipment()
        knights.append(new_knight)

    # -------------------------------------------------------------------------------
    # BATTLE:

    # 1 Lancelot vs Mordred:
    knights[0].battle_vs(knights[2])

    # 2 Arthur vs Red Knight:
    knights[1].battle_vs(knights[3])

    # Return battle results:
    results = {}
    for knight in knights:
        results[knight.name] = knight.hp

    return results
