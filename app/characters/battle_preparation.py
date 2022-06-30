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

        skills = {"hp": hp, "protection": protection, "power": power}
        if knights[character]["potion"] is not None:
            for key, value in skills.items():
                if key in knights[character]["potion"]["effect"]:
                    value += knights[character]["potion"]["effect"][key]
                    skills[key] = value

        knights_dict[character] = Knight(knights[character]['name'],
                                         skills["hp"],
                                         skills["protection"],
                                         skills["power"])

    return knights_dict
