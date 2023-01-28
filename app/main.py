from app.knights.data_knights import knights
from app.knights.ready_knights import create_knight


ready_knights = knights.copy()


def battle(ready_knights: dict) -> dict:

    for each in ready_knights:
        ready_knights[each] = create_knight(each, ready_knights)

    ready_knights["lancelot"].fight(ready_knights["mordred"])
    ready_knights["arthur"].fight(ready_knights["red_knight"])

    battle_result = {}

    for each in ready_knights.values():
        battle_result[each.name] = each.hp

    return battle_result


print(battle(ready_knights))
