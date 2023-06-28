from app.constants.property_list import PROPERTY_LIST


def battle_prepare(knight: dict, config: dict) -> None:
    def add_potion_effect(prop: str) -> None:
        potion_effect = knight["potion"]["effect"]
        if prop in potion_effect:
            knight[prop] += potion_effect[prop]

    knight = config[knight]

    # apply armour
    knight["protection"] = 0
    for armour in knight["armour"]:
        knight["protection"] += armour["protection"]

    # apply weapon
    knight["power"] += knight["weapon"]["power"]

    # apply potion if exist
    if knight["potion"] is not None:
        for prop in PROPERTY_LIST:
            add_potion_effect(prop)
