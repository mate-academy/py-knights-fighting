def fight(fighters: dict):
    combat(fighters["lancelot"], fighters["mordred"])
    combat(fighters["arthur"], fighters["red_knight"])
    return fighters


def combat(first, second):
    first.hp -= second.power - first.protection
    second.hp -= first.power - second.protection
    check_death(first, second)


def check_death(first, second):
    if first.hp < 0:
        first.hp = 0
    if second.hp < 0:
        second.hp = 0
