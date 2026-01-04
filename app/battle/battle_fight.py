def fight(knight1: object, knight2: object) -> None:

    knight1.hp -= knight2.power - abs(knight1.protection)
    knight2.hp -= knight1.power - abs(knight2.protection)

    for fighter in (knight1, knight2):
        if fighter.hp <= 0:
            fighter.hp = 0


if __name__ == "__main__":
    pass
