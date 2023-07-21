from app.knights import Knight
from app.list_knights import KNIGHTS


def battle(knights: dict) -> dict:
    # BATTLE PREPARATIONS:
    lancelot = Knight(*knights.get("lancelot").values())
    arthur = Knight(*knights.get("arthur").values())
    mordred = Knight(*knights.get("mordred").values())
    red_knight = Knight(*knights.get("red_knight").values())

    lancelot.prepare()
    arthur.prepare()
    mordred.prepare()
    red_knight.prepare()

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

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


print(battle(KNIGHTS))
