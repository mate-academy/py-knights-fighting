from app.knight.knight import Knight


def print_all() -> None:
    # print al Knights
    for knight, elem in Knight.knights.items():
        print(knight, " -> \n", elem)


def battle(knights_config: dict = None) -> str:

    # create knights from knights_config
    Knight.knights_load(knights_config)

    # BATTLE PREPARATIONS:
    print_all()

    # BATTLE:

    # 1 Lancelot vs Mordred:
    Knight.knights["lancelot"].fight(Knight.knights["mordred"])

    # 2 Arthur vs Red Knight:
    Knight.knights["arthur"].fight(Knight.knights["red_knight"])

    # Return battle results:
    result = Knight.battle_result()
    print("Battle result= ", result)
    return result


# main

if not ("knights_config" in locals() or "knights_config" in globals()):
    # load default values
    from app.load import knights_config

battle(knights_config)
