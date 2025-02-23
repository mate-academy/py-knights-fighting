from app.knight import Knight


def one_battle(first_knight: Knight, second_knight: Knight) -> None:
    first_knight.hp -= (second_knight.power - first_knight.protection)
    second_knight.hp -= (first_knight.power - second_knight.protection)

    # check if someone fell in battle
    first_knight.check_hp()
    second_knight.check_hp()


def battle(knights_config: dict) -> dict:
    # BATTLE PREPARATIONS:

    knights_list = []
    for name in knights_config:
        knights_list.append(Knight(knights_config[name]))

    # -------------------------------------------------------------------------------
    # BATTLE:
    # 1 Lancelot vs Mordred:
    one_battle(knights_list[0], knights_list[2])

    # 2 Arthur vs Red Knight:
    one_battle(knights_list[1], knights_list[3])

    # Return battle results:
    return {knight.name: knight.hp for knight in
            knights_list}
