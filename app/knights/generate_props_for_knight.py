from typing import Callable, Any
from app.knights.knight_constructor import KnightFighter


def apply_armour(func: Callable) -> Any:
    def wrapper(knight: KnightFighter) -> Any:
        protection = 0
        if knight.armour is not False:
            for value in knight.armour:
                protection += value["protection"]
        knight.armour = protection
        return func(knight)
    return wrapper


def apply_power(func: Callable) -> Any:
    def wrapper(knight: KnightFighter) -> Any:
        knight.power += knight.weapon["power"]
        return func(knight)
    return wrapper


def apply_potion(func: Callable) -> Any:
    def wrapper(knight: KnightFighter) -> Any:
        if knight.potion is not None:
            if "power" in knight.potion["effect"]:
                knight.power += knight.potion["effect"]["power"]
            if "protection" in knight.potion["effect"]:
                knight.armour += knight.potion["effect"]["protection"]
            if "hp" in knight.potion["effect"]:
                knight.hp += knight.potion["effect"]["hp"]
        return func(knight)
    return wrapper


@apply_armour
@apply_power
@apply_potion
def apply_values_before_fight(knight: KnightFighter) -> Any:
    return knight.__dict__


def knight_ready_for_fight(knight_dict: dict[KnightFighter]) -> Any:
    for knight in knight_dict:
        apply_values_before_fight(knight_dict[knight])
