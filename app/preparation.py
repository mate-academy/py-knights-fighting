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
                if "power" in attributes["potion"]["effect"]:
                    attributes["power"] += \
                        attributes["potion"]["effect"]["power"]

                if "protection" in attributes["potion"]["effect"]:
                    attributes["protection"] += \
                        attributes["potion"]["effect"]["protection"]

                if "hp" in attributes["potion"]["effect"]:
                    attributes["hp"] += attributes["potion"]["effect"]["hp"]
        return func(knights)
    return inner
