from app.action.battle import Arena
from app.entity.knights import Knights


def battle(knights_config: dict) -> dict:
    # BATTLE PREPARATIONS:
    lancelot = Knights.init_knight("lancelot", knights_config)
    arthur = Knights.init_knight("arthur", knights_config)
    mordred = Knights.init_knight("mordred", knights_config)
    red_knight = Knights.init_knight("red_knight", knights_config)

    # 1 Lancelot vs Mordred:
    Arena.fight(lancelot, mordred)
    # 2 Arthur vs Red Knight:
    Arena.fight(arthur, red_knight)

    result = {}

    result.update(lancelot.status()),
    result.update(arthur.status())
    result.update(mordred.status())
    result.update(red_knight.status())
    # Return battle results:
    return result
