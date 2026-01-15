from app.knights.settings import KNIGHTS
from app.knights.knight import Knight


def battle(knights_config: dict) -> dict:
    # BATTLE PREPARATIONS:

    # lancelot
    lancelot = Knight(**knights_config["lancelot"])
    lancelot.prepare_for_fight()

    # arthur
    arthur = Knight(**knights_config["arthur"])
    arthur.prepare_for_fight()

    # mordred
    mordred = Knight(**knights_config["mordred"])
    mordred.prepare_for_fight()

    # red_knight
    red_knight = Knight(**knights_config["red_knight"])
    red_knight.prepare_for_fight()

    # -------------------------------------------------------------------------------
    # BATTLE:

    lancelot.fight(mordred)
    arthur.fight(red_knight)

    # Return battle results:
    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


print(battle(KNIGHTS))
