def fight(first_heroy, second_heroy):
    first_heroy.hp -= (second_heroy.power - first_heroy.protect)
    second_heroy.hp -= (first_heroy.power - second_heroy.protect)

    if first_heroy.hp <= 0:
        first_heroy.hp = 0

    if second_heroy.hp <= 0:
        second_heroy.hp = 0

    return first_heroy, second_heroy
