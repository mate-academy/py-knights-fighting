def start_fight(knights: list) -> None:
    first_pair = knights[0], knights[2]
    second_pair = knights[1], knights[3]

    for pair in first_pair, second_pair:
        first_knight = pair[0]
        second_knight = pair[1]
        first_knight.hp -= (second_knight.power - first_knight.protection)
        second_knight.hp -= (first_knight.power - second_knight.protection)
