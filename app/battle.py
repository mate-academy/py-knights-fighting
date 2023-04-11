from participant.knight import Knight


def battle(knights_config: dict) -> dict:
    # BATTLE PREPARATIONS:

    # lancelot
    lancelot = Knight(knights_config["lancelot"])
    lancelot.apply_all_equipment()

    # arthur
    arthur = Knight(knights_config["arthur"])
    arthur.apply_all_equipment()

    # mordred
    mordred = Knight(knights_config["mordred"])
    mordred.apply_all_equipment()

    # red_knight
    red_knight = Knight(knights_config["red_knight"])
    red_knight.apply_all_equipment()

    # -------------------------------------------------------------------------------
    # BATTLE:

    # 1 Lancelot vs Mordred:
    lancelot.battle_vs(mordred)

    # 2 Arthur vs Red Knight:
    arthur.battle_vs(red_knight)

    # Return battle results:
    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }
