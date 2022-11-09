from app.Knights.Knight import Knight


def battle(knights_config: dict) -> dict:
    knights = {knight: Knight(knights_config[knight])
               for knight in knights_config}

    for knight in knights.values():
        knight.ready_for_war()

    Knight.fight(knights["lancelot"], knights["mordred"])
    Knight.fight(knights["arthur"], knights["red_knight"])

    return {knight.name: knight.hp for knight in knights.values()}
