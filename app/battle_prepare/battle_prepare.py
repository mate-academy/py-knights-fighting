from app.constants.lists import PROPERTY_LIST


def battle_prepare(knight: dict) -> None:
    def add_potion_effect(prop: str) -> None:
        potion_effect = knight.get("potion", {}).get("effect")
        if prop in potion_effect:
            knight[prop] += potion_effect[prop]

    # apply armour
    knight["protection"] = 0
    for armour in knight["armour"]:
        knight["protection"] += armour["protection"]

    # apply weapon
    knight["power"] += knight.get("weapon", {}).get("power")

    # apply potion if exist
    if "potion" in knight and knight["potion"] is not None:
        for prop in PROPERTY_LIST:
            add_potion_effect(prop)
