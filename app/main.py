from app.preparation_for_battle import preparation_for_battle
from app.battle import duel, check_hp
from app.creation_of_knights import creation_of_knights, KNIGHTS


def battle(knights: dict) -> dict:
    players = creation_of_knights(knights)
    result = {}
    for knight in players.values():

        preparation_for_battle(knight)

    # Lancelot VS Mordred
    duel(players["lancelot"], players["mordred"])
    # Artur VS Red Knight
    duel(players["arthur"], players["red_knight"])

    check_hp(players)

    for knight in players.values():
        result[knight.name] = knight.hp

    return result


print(battle(KNIGHTS))
