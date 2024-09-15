from typing import Callable


def drink_potion(knight: Callable, potions: dict | None) -> None:
    if potions is not None:
        if "power" in potions["effect"]:
            knight.power += potions["effect"]["power"]
        if "protection" in potions["effect"]:
            knight.protection += potions["effect"]["protection"]
        if "hp" in potions["effect"]:
            knight.hp += potions["effect"]["hp"]
