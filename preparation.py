def apply_armour(knight):
    knight["protection"] = sum(a["protection"] for a in knight["armour"])


def apply_weapon(knight):
    knight["power"] += knight["weapon"]["power"]


def apply_potion(knight):
    if knight["potion"] is not None:
        for effect, value in knight["potion"]["effect"].items():
            if effect in knight:
                knight[effect] += value


def prepare_knights(knights_config):
    for knight in knights_config.values():
        apply_armour(knight)
        apply_weapon(knight)
        apply_potion(knight)
    return knights_config
