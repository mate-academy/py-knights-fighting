def apply_armour(knight):
    knight["protection"] = 0
    for protection in knight["armour"]:
        knight["protection"] += protection["protection"]


def apply_weapon(knight):
    knight["power"] += knight["weapon"]["power"]


def apply_potion_if_exist(knight):
    if knight["potion"] is not None:
        if "power" in knight["potion"]["effect"]:
            knight["power"] += knight["potion"]["effect"]["power"]

        if "protection" in knight["potion"]["effect"]:
            knight["protection"] += knight["potion"]["effect"]["protection"]

        if "hp" in knight["potion"]["effect"]:
            knight["hp"] += knight["potion"]["effect"]["hp"]


def train(*args):
    for knight in args:
        apply_armour(knight)
        apply_weapon(knight)
        apply_potion_if_exist(knight)
