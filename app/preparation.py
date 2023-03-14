from typing import Callable


def preparation(func: Callable) -> Callable:
    def inner(knights: dict) -> Callable:
        for knight, attributes in knights.items():

            # apply weapon
            attributes["power"] += attributes["weapon"]["power"]

            # apply armour
            attributes["protection"] = 0
            if len(attributes["armour"]) > 0:
                for attr in attributes["armour"]:
                    attributes["protection"] += attr["protection"]

            # apply potion if exist
            if attributes["potion"] is not None:
                for attribute in ["power", "protection", "hp"]:
                    if attribute in attributes["potion"]["effect"]:
                        attributes[attribute] += \
                            attributes["potion"]["effect"][attribute]

        return func(knights)
    return inner
