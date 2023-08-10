from app.battle.apply_buffs import stats
from app.battle.life_checker import life_check
from app.battle.damage_system import damage


def combat(knights: dict) -> dict:
    arthur = knights["Arthur"]
    lancelot = knights["Lancelot"]
    mordred = knights["Mordred"]
    red_knight = knights["Red Knight"]

    # calculate stats of every knight with buffs
    stats(arthur)
    stats(lancelot)
    stats(mordred)
    stats(red_knight)
    # -------------------------------------------------------------------------------
    # BATTLE:

    # 1 Lancelot vs Mordred:
    damage(lancelot, mordred)

    # check if someone fell in battle
    life_check(lancelot)
    life_check(mordred)

    # 2 Arthur vs Red Knight:
    damage(arthur, red_knight)

    # check if someone fell in battle
    life_check(arthur)
    life_check(red_knight)

    return {
        "Lancelot": lancelot.hp,
        "Arthur": arthur.hp,
        "Mordred": mordred.hp,
        "Red Knight": red_knight.hp
    }
