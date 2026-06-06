from app.knights import Knights
from app.config import KNIGHTS


def battle(knightsconfig: dict) -> dict:
    knights = {}
    for key, value in knightsconfig.items():
        knight = Knights(value["name"],
                         value["hp"],
                         value["armour"],
                         value["power"],
                         value["weapon"],
                         value["potion"])
        knights[key] = knight

    for key, value in knights.items():
        value.prepare_for_battle()

    lancelot = knights["lancelot"]
    arthur = knights["arthur"]
    mordred = knights["mordred"]
    red_knight = knights["red_knight"]

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
        lancelot.name: lancelot.hp, mordred.name: mordred.hp,
        arthur.name: arthur.hp, red_knight.name: red_knight.hp
    }


print(battle(KNIGHTS))
