from app.knights.knights import Knights


def create_knights(knights: dict) -> list:
    knights_list = []
    for knight in knights.values():
        knight_name = knight["name"]
        knight_power = knight["power"]
        knight_hp = knight["hp"]
        knight_protection = 0
        for armour in knight["armour"]:
            knight_protection += armour["protection"]
        knight_power += knight["weapon"]["power"]
        if knight["potion"] is not None:
            if "power" in knight["potion"]["effect"]:
                knight_power += knight["potion"]["effect"]["power"]

            if "protection" in knight["potion"]["effect"]:
                knight_protection += knight["potion"]["effect"]["protection"]

            if "hp" in knight["potion"]["effect"]:
                knight_hp += knight["potion"]["effect"]["hp"]
        knight_person = Knights(knight_name, {
            "hp": knight_hp,
            "power": knight_power,
            "protection": knight_protection
        })
        knights_list.append(knight_person)
    return knights_list
