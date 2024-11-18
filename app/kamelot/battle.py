from app.kamelot.knight import Knight


def duel(*knights: Knight | list[Knight] | tuple[Knight, Knight]) -> dict:
    """
    The logic of a duel between two knights.
    """
    if len(knights) == 2:
        knight1, knight2 = knights
    else:
        knight1, knight2 = knights[0]

    knight1.battle_preparations()
    knight2.battle_preparations()

    knight2.make_damage(knight1)
    knight1.make_damage(knight2)

    return {
        knight1.name: knight1.hp,
        knight2.name: knight2.hp
    }


def standings(*knights: Knight) -> dict:
    """
    Create a dictionary of results based on the sample in the task.
    """
    standings = {}

    for knight in knights:
        standings.update(knight.get_hp())

    return standings
