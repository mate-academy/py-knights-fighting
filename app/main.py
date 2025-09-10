from app.action.battle import Arena
from app.entity.knights import Knights


def battle(knights_config: dict) -> dict:
    # BATTLE PREPARATIONS:
    knights = {name : Knights.init_knight(name, knights_config)
               for name in knights_config}

    # 1 Lancelot vs Mordred:
    Arena.fight(knights["lancelot"], knights["mordred"])
    # 2 Arthur vs Red Knight:
    Arena.fight(knights["arthur"], knights["red_knight"])

    result = {}

    for knight in knights:
        result.update({knights[knight].name : knights[knight].health})
    # Return battle results:
    return result
