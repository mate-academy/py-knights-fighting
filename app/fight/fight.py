def fight(first, second):
    first.hp -= second.power - first.protection
    second.hp -= first.power - second.protection

    # check if someone fell in fight
    if first.hp <= 0:
        first.hp = 0

    if second.hp <= 0:
        second.hp = 0
