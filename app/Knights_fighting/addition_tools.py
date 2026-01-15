from typing import Callable


def magic_upgrades(__init__: Callable) -> Callable:
    def wrapper(self: None, input_dict: dict) -> None:
        input_dict["protection"] = sum(part["protection"]
                                       for part in input_dict["armour"])
        input_dict["power"] += input_dict["weapon"]["power"]
        if input_dict["potion"]:
            potion = input_dict["potion"]["effect"]

            for name in potion.keys():
                input_dict[name] += potion[name]

        __init__(self, input_dict)

    return wrapper
