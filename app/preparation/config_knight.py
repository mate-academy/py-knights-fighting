from app.preparation.create_knight import Knight


def config_knight(all_knights: dict) -> list:
    knight_list = []
    for knight in all_knights:
        knight = all_knights[knight]
        person = Knight(knight["name"], knight["power"], knight["hp"])

        # apply armour
        person.protection = 0
        for armour in knight["armour"]:
            person.protection += armour["protection"]

        # apply weapon
        person.power += knight["weapon"]["power"]
        knight_list.append(person)

        # apply potion
        if knight["potion"] is not None:
            if "power" in knight["potion"]["effect"]:
                person.power += knight["potion"]["effect"]["power"]

            if "protection" in knight["potion"]["effect"]:
                person.protection += knight["potion"]["effect"]["protection"]

            if "hp" in knight["potion"]["effect"]:
                person.hp += knight["potion"]["effect"]["hp"]

    return knight_list
