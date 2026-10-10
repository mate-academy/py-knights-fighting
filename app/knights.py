def prepare_knight(knight: dict) -> None:
    knight["protection"] = sum(
        item["protection"] for item in knight["armour"]
    )

    knight["power"] += knight["weapon"]["power"]

    potion = knight["potion"]
    if potion is not None:
        for stat, bonus in potion["effect"].items():
            knight[stat] += bonus
