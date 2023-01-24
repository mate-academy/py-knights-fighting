from typing import Callable, Any

from app.knights.knight_constructor import KnightFighter


def armour(func: Callable) -> Any:
    def wrapper(item: KnightFighter) -> Any:
        protection = 0
        if item.armour is not False:
            for value in item.armour:
                protection += value["protection"]
        item.armour = protection
        return func(item)
    return wrapper


def power(func: Callable) -> Any:
    def wrapper(item: KnightFighter) -> Any:
        item.power += item.weapon["power"]
        return func(item)
    return wrapper


def potion_apply(func: Callable) -> Any:
    def wrapper(item: KnightFighter) -> Any:
        if item.potion is not None:
            if "power" in item.potion["effect"]:
                item.power += item.potion["effect"]["power"]
            if "protection" in item.potion["effect"]:
                item.armour += item.potion["effect"]["protection"]
            if "hp" in item.potion["effect"]:
                item.hp += item.potion["effect"]["hp"]
        return func(item)
    return wrapper


@armour
@power
@potion_apply
def apply_values_before_fight(knight: KnightFighter) -> Any:
    return knight.__dict__


def knight_ready_for_fight(knight_dict: list) -> Any:
    for fighter in knight_dict:
        apply_values_before_fight(knight_dict[fighter])
