from app.data.knights import KNIGHTS
from app.knights_fighting.knight import Knight


def prepare_knight(knight_data: dict) -> Knight:
    knight = Knight(
        knight_data["name"],
        knight_data["power"],
        knight_data["hp"]
    )
    knight.prepare(
        knight_data["weapon"],
        knight_data["armour"],
        knight_data["potion"]
    )
    return knight


def battle(knights_data: dict) -> dict:
    # BATTLE PREPARATIONS:
    lancelot = prepare_knight(knights_data["lancelot"])
    arthur = prepare_knight(knights_data["arthur"])
    mordred = prepare_knight(knights_data["mordred"])
    red_knight = prepare_knight(knights_data["red_knight"])

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


print(battle(KNIGHTS))
