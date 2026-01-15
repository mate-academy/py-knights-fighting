from participant.knight import Knight


def battle(knights_config: dict) -> dict:
    # BATTLE PREPARATIONS:
    knights = {}

    # create knights and apply equipment
    for name, config in knights_config.items():
        new_knight = Knight(config)
        new_knight.apply_all_equipment()
        knights[name] = new_knight

    # -------------------------------------------------------------------------------
    # BATTLE:

    # 1 Lancelot vs Mordred:
    knights["lancelot"].battle_vs(knights["mordred"])

    # 2 Arthur vs Red Knight:
    knights["arthur"].battle_vs(knights["red_knight"])

    # Return battle results:
    results = {}
    for knight in knights.values():
        results[knight.name] = knight.hp
        knight.check_hp()

    return results
