from app.preparing_knights.create import create_knights
from app.preparing_knights.knights import Knights


def battle(knights: dict) -> dict:
    # create instances of knights and recalulate stats:
    create_knights(knights)
    # prepare fighters:
    lancelot = Knights.knights_inst["Lancelot"]
    mordred = Knights.knights_inst["Mordred"]
    arthur = Knights.knights_inst["Arthur"]
    red_knight = Knights.knights_inst["Red Knight"]

    # battles:
    # 1 Lancelot vs Mordred:
    lancelot.hp -= mordred.power - lancelot.protection
    mordred.hp -= lancelot.power - mordred.protection
    # 2 Arthur vs Red Knight:
    arthur.hp -= red_knight.power - arthur.protection
    red_knight.hp -= arthur.power - red_knight.protection

    # recalculating 'hp' all knights after the fight:
    Knights.recount_hp()
    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }
