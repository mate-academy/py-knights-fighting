from app.knights_config import KNIGHTS
from app.knight_crearing import create_knight


def battle(knights: dict) -> dict:
    lancelot = create_knight(knights["lancelot"])
    lancelot.apply_armour(knights["lancelot"])
    lancelot.apply_weapon(knights["lancelot"])
    lancelot.apply_potion(knights["lancelot"]["potion"])

    arthur = create_knight(knights["arthur"])
    arthur.apply_armour(knights["arthur"])
    arthur.apply_weapon(knights["arthur"])
    arthur.apply_potion(knights["arthur"]["potion"])

    mordred = create_knight(knights["mordred"])
    mordred.apply_armour(knights["mordred"])
    mordred.apply_weapon(knights["mordred"])
    mordred.apply_potion(knights["mordred"]["potion"])

    red_knight = create_knight(knights["red_knight"])
    red_knight.apply_armour(knights["red_knight"])
    red_knight.apply_weapon(knights["red_knight"])
    red_knight.apply_potion(knights["red_knight"]["potion"])

    lancelot.hp -= mordred.power - lancelot.protection
    mordred.hp -= lancelot.power - mordred.protection

    if lancelot.hp <= 0:
        lancelot.hp = 0

    if mordred.hp <= 0:
        mordred.hp = 0

    arthur.hp -= red_knight.power - arthur.protection
    red_knight.hp -= arthur.power - red_knight.protection

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
