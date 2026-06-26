from app.knights.knights import KNIGHTS
from app.knights.knight import Knight
from app.logic.fight import get_fight
from app.logic.check_hp import check_hp


def battle(knights_config: dict) -> dict:
    # BATTLE PREPARATIONS:

    # lancelot
    lancelot = Knight(knights_config["lancelot"])
    lancelot.apply_potion()

    # arthur
    arthur = Knight(knights_config["arthur"])
    arthur.apply_potion()

    # mordred
    mordred = Knight(knights_config["mordred"])
    mordred.apply_potion()

    # red_knight
    red_knight = Knight(knights_config["red_knight"])
    red_knight.apply_potion()

    # -------------------------------------------------------------------------------
    # BATTLE:

    # 1 Lancelot vs Mordred:
    get_fight(lancelot, mordred)
    # 2 Arthur vs Red Knight:
    get_fight(arthur, red_knight)

    # check if someone fell in battle
    check_hp(lancelot)
    check_hp(mordred)
    check_hp(arthur)
    check_hp(red_knight)

    # Return battle results:
    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


print(battle(KNIGHTS))
