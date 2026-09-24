from app.knight import prepare_knights
# -------------------------------------------------------------------------------
# BATTLE:
# 1 Lancelot vs Mordred:


def battle(config: dict) -> dict:
    knights = prepare_knights(config)

    lancelot = knights["lancelot"]
    mordred = knights["mordred"]

    arthur = knights["arthur"]
    red_knight = knights["red_knight"]

    mordred.attack(lancelot)
    lancelot.attack(mordred)

    red_knight.attack(arthur)
    arthur.attack(red_knight)

    # return battle results:
    return {
        lancelot.name : lancelot.hp,
        arthur.name : arthur.hp,
        mordred.name : mordred.hp,
        red_knight.name : red_knight.hp,
    }
