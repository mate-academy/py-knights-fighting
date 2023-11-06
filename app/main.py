from app.check_stats import Battle as Battle
from app.knights_data import KNIGHTS


def battle(knights: dict) -> dict:
    mordred = Battle(knights["mordred"])
    lancelot = Battle(knights["lancelot"])
    red_knight = Battle(knights["red_knight"])
    arthur = Battle(knights["arthur"])

    for knight in [lancelot, arthur, mordred, red_knight]:
        knight.check_all_attributes()

    Battle.battle_knight(arthur, red_knight)
    Battle.battle_knight(lancelot, mordred)
    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


print(battle(KNIGHTS))
