
def prepare_knight(knight: dict) -> None:
    knight["protection"] = sum(
        attribut["protection"]
        for attribut in
        knight["armour"])
    knight["power"] += knight["weapon"]["power"]
    if knight["potion"]:
        for effect in ["power", "protection", "hp"]:
            if effect in knight["potion"]["effect"]:
                knight[effect] += knight["potion"]["effect"][effect]
