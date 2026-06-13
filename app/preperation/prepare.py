from app.knights.config import KnightDict


def prepare_knight(knight: KnightDict) -> None:
    knight["protection"] = sum(
        armour["protection"] for armour in knight["armour"]
    )
    knight["power"] += knight["weapon"]["power"]

    if knight["potion"] is not None:
        for stat, value in knight["potion"]["effect"].items():
            knight[stat] += value
