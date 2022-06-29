from app.characters.knights import Knight


def battle_preparation(knights):
    knights_dict = {}

    for character in knights:
        hp = knights[character]["hp"]

        protection = 0
        for armour in knights[character]["armour"]:
            protection += armour["protection"]

        power = knights[character]["power"] +\
            knights[character]["weapon"]["power"]

        if knights[character]["potion"] is not None:
            if "power" in knights[character]["potion"]["effect"]:
                power += knights[character]["potion"]["effect"]["power"]

            if "protection" in knights[character]["potion"]["effect"]:
                protection += \
                    knights[character]["potion"]["effect"]["protection"]

            if "hp" in knights[character]["potion"]["effect"]:
                hp += knights[character]["potion"]["effect"]["hp"]

        knights_dict[character] = Knight(knights[character]['name'],
                                         hp, protection, power)

    return knights_dict
