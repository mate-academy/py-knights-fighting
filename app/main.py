from app.battle.knights_dict import knights
from app.battle.Knights import Knight
from app.battle.types import KnightConfig


def battle(knights_config: dict[str, KnightConfig]) -> dict:
    # BATTLE PREPARATIONS:

    # lancelot
    lancelot = Knight(knights_config["lancelot"])
    arthur = Knight(knights_config["arthur"])
    mordred = Knight(knights_config["mordred"])
    red_knight = Knight(knights_config["red_knight"])

    # -------------------------------------------------------------------------------
    # BATTLE:

    # 1 Lancelot vs Mordred:
    lancelot.fight_with(mordred)

    arthur.fight_with(red_knight)
    # 2 Arthur vs Red Knight:

    # Return battle results:
    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        red_knight.name: red_knight.hp,
        mordred.name: mordred.hp,
    }


print(battle(knights))
