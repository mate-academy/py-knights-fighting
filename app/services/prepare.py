def prepare(knight_config: dict) -> dict:
    prepared = {}
    for name, knight in knight_config.items():
        prepared[name] = prepare_knight(knight)
    return prepared


def prepare_knight(knight: dict) -> dict:
    knight["protection"] = sum(a["protection"] for a in knight["armour"])
    knight["power"] += knight["weapon"]["power"]

    if knight["potion"] is not None:
        effect = knight["potion"]["effect"]
        for stat in ["hp", "power", "protection"]:
            knight[stat] += effect.get(stat, 0)
    return knight
