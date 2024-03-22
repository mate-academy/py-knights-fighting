from app.character.knight import Knight


def battle(basic_knights: dict) -> dict:
    knights_list = [Knight(**basic_knights[knight])
                    for knight in basic_knights]

    # gear_up() is to get weapon, armour, drink pots
    for knight in knights_list:
        knight.gear_up()

    # fight with each other 1st vs 3rd, 2nd vs 4th
    for knights_list_index in range(len(knights_list) // 2):
        first_fighter = knights_list[knights_list_index]
        second_fighter = knights_list[knights_list_index + 2]

        first_fighter.hp -= (second_fighter.power
                             - first_fighter.protection)
        second_fighter.hp -= (first_fighter.power
                              - second_fighter.protection)

    return {
        knights_list[knight_index].name: knights_list[knight_index].hp
        if knights_list[knight_index].hp >= 0 else 0
        for knight_index in range(len(knights_list))
    }
