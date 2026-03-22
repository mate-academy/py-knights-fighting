from knights.knight import Knight


def start_fight(knights: list[Knight]) -> None:
    knights[0].defend(knights[1])
    knights[1].defend(knights[0])

    knights[2].defend(knights[3])
    knights[3].defend(knights[2])
