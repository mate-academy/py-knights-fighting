def prepare_to_fight(knight: dict) -> None:
    """Apply all effects (armor, weapon, potion) to a knight."""
    # Initialize protection
    try:
        knight.get(knight["protection"], False)
    except KeyError:
        knight["protection"] = 0

    # Apply armor
    for armor_piece in knight["armour"]:
        knight["protection"] += armor_piece["protection"]

    # Apply weapon
    knight["power"] += knight["weapon"]["power"]

    # Apply potion if exists
    if knight["potion"] is not None:
        for stat, value in knight["potion"]["effect"].items():
            if stat == "protection":
                knight["protection"] += value
            else:
                knight[stat] = max(0, knight[stat] + value)
