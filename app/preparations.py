from typing import Dict, Any


def prepare_knight(knight: Dict[str, Any]) -> None:
    # apply armour
    knight["protection"] = sum(
        armour["protection"] for armour in knight["armour"]
    )

    knight["power"] += knight["weapon"]["power"]

    potion: Any | None = knight.get("potion")
    if potion:
        for stat, delta in potion["effect"].items():
            if stat in knight:
                knight[stat] += delta
