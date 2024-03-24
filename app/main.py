from app.preparing_knights.create import create_knights
from app.preparing_knights.knights import Knights


def battle(knights: dict) -> dict:
    create_knights(knights)

    lancelot = Knights.knights_inst["Lancelot"]
    mordred = Knights.knights_inst["Mordred"]
    arthur = Knights.knights_inst["Arthur"]
    red_knight = Knights.knights_inst["Red Knight"]

    lancelot.hp -= mordred.power - lancelot.protection
    mordred.hp -= lancelot.power - mordred.protection
    arthur.hp -= red_knight.power - arthur.protection
    red_knight.hp -= arthur.power - red_knight.protection

    Knights.recount_hp()
    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }
