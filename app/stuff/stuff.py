def used_armor(knight: dict):
    knight["protection"] = 0
    if knight["armour"]:
        for key in knight["armour"]:
            knight["protection"] += key["protection"]


def used_weapon(knight: dict):
    knight["power"] += knight["weapon"]["power"]


def used_potion(knight: dict):
    if knight["potion"]:
        for boosts_name, boosts_value in knight["potion"]["effect"].items():
            if boosts_name in knight:
                knight[boosts_name] += boosts_value
