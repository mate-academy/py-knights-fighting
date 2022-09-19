def brawl(first, second) -> None:
    first.hp -= second.power - first.protection
    if first.hp <= 0:
        first.hp = 0
    second.hp -= first.power - second.protection
    if second.hp <= 0:
        second.hp = 0
