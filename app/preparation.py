from typing import Callable


def preparation(func: Callable) -> Callable:
    def inner(knights: dict) -> Callable:
        for knight, attributes in knights.items():

            # apply weapon
            attributes["power"] += attributes["weapon"]["power"]

            # apply armour
            attributes["protection"] = 0
            if len(attributes["armour"]) > 0:
                for parameter in attributes["armour"]:
                    attributes["protection"] += parameter["protection"]

            # apply potion if exist
            if (attributes["potion"] is not None
                    and "effect" in attributes["potion"]):
                potion_effects = attributes["potion"]["effect"]

                for attribute in potion_effects:
                    if attribute == "power":
                        attributes["power"] += potion_effects[attribute]
                    elif attribute == "protection":
                        attributes["protection"] += potion_effects[attribute]
                    elif attribute == "hp":
                        attributes["hp"] += potion_effects[attribute]

        return func(knights)
    return inner
