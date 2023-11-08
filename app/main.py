from app.check_stats import Knight, Battle
from app.knights_data import KNIGHTS


def battle(knights: dict) -> dict:
    mordred = Knight(knights["mordred"])
    lancelot = Knight(knights["lancelot"])
    red_knight = Knight(knights["red_knight"])
    arthur = Knight(knights["arthur"])

    for knight in [lancelot, arthur, mordred, red_knight]:
        knight.check_weapon()
        knight.check_armour()
        knight.check_potion()

    Battle.battle_knight(arthur, red_knight)
    Battle.battle_knight(lancelot, mordred)
    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


print(battle(KNIGHTS))
