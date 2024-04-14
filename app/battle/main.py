from app.knight.knights import KNIGHTS
from app.knight.knight_class import Knight


def battle(knights_config: dict) -> dict:
    lancelot = Knight(knights_config["lancelot"])
    mordred = Knight(knights_config["mordred"])
    arthur = Knight(knights_config["arthur"])
    red_knight = Knight(knights_config["red_knight"])
    knights = [lancelot, mordred, arthur, red_knight]

    for knight in knights:
        if knight.potion is not None:
            if "power" in knight.potion.effect:
                knight.power += knight.potion.effect["power"]

            if "protection" in knight.potion.effect:
                knight.protection += knight.potion.effect["protection"]

            if "hp" in knight.potion.effect:
                knight.hp += knight.potion.effect["hp"]

    lancelot.hp -= mordred.power - lancelot.protection
    mordred.hp -= lancelot.power - mordred.protection
    arthur.hp -= red_knight.power - arthur.protection
    red_knight.hp -= arthur.power - red_knight.protection

    if lancelot.hp <= 0:
        lancelot.hp = 0

    if mordred.hp <= 0:
        mordred.hp = 0

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
