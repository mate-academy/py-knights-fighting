from app.preparation_for_battle import preparation_for_battle
from app.battle import duel, check_hp
from app.creation_of_knights import creation_of_knights, KNIGHTS


def battle(knights: dict) -> dict:
    players = creation_of_knights(knights)
    result = {}
    for knight in players:

        preparation_for_battle(knight)

    # Lancelot VS Mordred
    duel(players[0], players[2])
    # Artur VS Red Knight
    duel(players[1], players[3])

    check_hp(players)

    for knight in players:
        result[knight.name] = knight.hp

    return result


print(battle(KNIGHTS))
