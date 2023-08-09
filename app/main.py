from app.knights_config import get_knights, dict_to_classes
from app.arena import Arena
from app.knights import Knight


def battle(knights: list["Knight"]| dict) -> dict:

    if not isinstance(knights, list):
        knights = dict_to_classes(knights)

    for knight in knights:
        knight.prepare_for_battle()

    arena = Arena()
    arena.fight(knights[0], knights[1])
    arena.fight(knights[1], knights[2])
    arena.check_hp(knights)

    match_results = {}
    for knight in knights:
        match_results[knight.name] = knight.hp

    return match_results


if __name__ == "__main__":
    print(battle(get_knights()))
