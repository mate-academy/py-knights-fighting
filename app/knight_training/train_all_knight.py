def apply_armour(knight):
    knight["protection"] = 0
    for armour in knight["armour"]:
        knight["protection"] += armour["protection"]


def apply_weapon(knight):
    knight["power"] += knight["weapon"]["power"]


def apply_potion_if_exist(knight):
    if knight["potion"] is not None:
        for magic in ("power", "protection", "hp"):
            if magic in knight["potion"]["effect"]:
                knight[magic] += knight["potion"]["effect"][magic]


def train(*args):
    for knight in args:
        apply_armour(knight)
        apply_weapon(knight)
        apply_potion_if_exist(knight)
