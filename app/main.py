from app.fight.battle import versus, check_if_die
from app.fight.knight import Knight
from app.fight.create_knights import create_knights
from app.fight.KNIGHTSCONST import KNIGHTS


# -------------------------------------------------------------------------------
# BATTLE:
def battle(knights):
    # lancelot preparing
    lancelot = create_knights(knights["lancelot"])
    lancelot.apply_weapon()
    lancelot.apply_armor()
    lancelot.apply_potion()

    # arthur preparing
    arthur = create_knights(knights["arthur"])
    arthur.apply_weapon()
    arthur.apply_armor()
    arthur.apply_potion()

    # mordred preparing
    mordred = create_knights(knights["mordred"])
    mordred.apply_weapon()
    mordred.apply_armor()
    mordred.apply_potion()

    # red_knight preparing
    red_knight = create_knights(knights["red_knight"])
    red_knight.apply_weapon()
    red_knight.apply_armor()
    red_knight.apply_potion()

    # 1 Lancelot vs Mordred:
    versus(lancelot, mordred)

    # check if someone fell in fighting
    check_if_die(lancelot)
    check_if_die(mordred)

    # 2 Arthur vs Red Knight:
    versus(arthur, red_knight)

    # check if someone fell in fighting
    check_if_die(arthur)
    check_if_die(red_knight)

    result = {}

    for knight in Knight.knights:
        result[knight.name] = knight.hp
    return result


# Return fighting results:

print(battle(KNIGHTS))
