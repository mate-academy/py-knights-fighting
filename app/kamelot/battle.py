from app.kamelot.knight import Knight


def duel(*knights: Knight | list[Knight] | tuple[Knight, Knight]) -> dict:
    """
    The logic of a duel between two knights.
    First, I check the correctness of the arguments.
    """
    if not (
            len(knights) == 2
            and isinstance(knights[0], Knight)
            and isinstance(knights[1], Knight)
            or
            len(knights) == 1
            and isinstance(knights[0][0], Knight)
            and isinstance(knights[0][1], Knight)
    ):
        raise ValueError(f"The duel function accepts only 2 knights of the 'Knight' type!"
                         f"Example:"
                         f"\tduel(knight1: Knight, knight2: Knight)"
                         f"\tduel(knights: list[Knight1, Knight2])"
                         f"\tduel(knights: tuple(Knight1, Knight2)")

    if len(knights) == 2:
        knight1, knight2 = knights
    else:
        knight1, knight2 = knights[0]

    knight1.hp -= knight2.power - knight1.protection
    knight2.hp -= knight1.power - knight2.protection

    if knight1.hp <= 0:
        knight1.hp = 0

    if knight2.hp <= 0:
        knight2.hp = 0

    return {
        knight1.name: knight1.hp,
        knight2.name: knight2.hp
    }
