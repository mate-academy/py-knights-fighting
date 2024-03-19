from app.Knights.knights_stats import Characters


def battle(basic_knights: dict) -> dict:
    knights_list = [Characters(**basic_knights[knight])
                    for knight in basic_knights]

    # gear_up() is to get weapon, armour, drink pots
    [knight.gear_up() for knight in knights_list]

    # fight with each other 1st vs 3rd, 2nd vs 4th
    for i in range(len(knights_list) // 2):
        knights_list[i].hp -= (knights_list[i + 2].power
                               - knights_list[i].protection)
        knights_list[i + 2].hp -= (knights_list[i].power
                                   - knights_list[i + 2].protection)

    return {
        knights_list[i].name: knights_list[i].hp
        if knights_list[i].hp >= 0 else 0
        for i in range(len(knights_list))
    }
