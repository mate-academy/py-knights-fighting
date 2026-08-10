from app.knight import Knights
from app.knights_stats.lancelot_stats import LANCELOT
from app.knights_stats.arthur_stats import ARTHUR
from app.knights_stats.mordred_stats import MORDRED
from app.knights_stats.red_knight_stats import RED_KNIGHT


def battle(config: dict) -> dict:
    lancelot = Knights.from_dict(config["lancelot"])
    arthur = Knights.from_dict(config["arthur"])
    mordred = Knights.from_dict(config["mordred"])
    red_knight = Knights.from_dict(config["red_knight"])

    # -------------------------------------------------------------------------------
    # BATTLE:

    # 1 Lancelot vs Mordred:
    lancelot.hp -= mordred.power - lancelot.protection
    mordred.hp -= lancelot.power - mordred.protection

    # check if someone fell in battle
    if lancelot.hp <= 0:
        lancelot.hp = 0

    if mordred.hp <= 0:
        mordred.hp = 0

    # 2 Arthur vs Red Knight:
    arthur.hp -= red_knight.power - arthur.protection
    red_knight.hp -= arthur.power - red_knight.protection

    # check if someone fell in battle
    if arthur.hp <= 0:
        arthur.hp = 0

    if red_knight.hp <= 0:
        red_knight.hp = 0

    # Return battle results:
    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


config = {
    "lancelot": LANCELOT["lancelot"],
    "arthur": ARTHUR["arthur"],
    "mordred": MORDRED["mordred"],
    "red_knight": RED_KNIGHT["red_knight"],
}

print(battle(config))
