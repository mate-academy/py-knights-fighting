"""Knight stats preparation for battle (armour, weapon, potion)."""


def prepare_knight_for_battle(knight: dict) -> None:
    """
    Apply armour, weapon and potion to knight stats in place.
    Expects a mutable copy of knight config; base protection is 0.
    """
    knight["protection"] = 0
    for armour_part in knight["armour"]:
        knight["protection"] += armour_part["protection"]

    knight["power"] += knight["weapon"]["power"]

    if knight["potion"] is not None:
        effect = knight["potion"]["effect"]
        for stat in ("power", "protection", "hp"):
            if stat in effect:
                knight[stat] += effect[stat]
