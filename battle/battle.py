from knights.knight import Knight


def start_fight(knights: list[Knight]) -> None:

    for i in range(0, len(knights), 2):
        k1 = knights[i]
        k2 = knights[i + 1]

        k1.defend(k2)
        k2.defend(k1)
