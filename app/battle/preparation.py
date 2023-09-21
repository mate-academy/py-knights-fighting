from __future__ import annotations
from app.classes.class_knights import Knights


def protection_calc(knight: Knights, armour: list[dict]) -> None:
    for part in armour:
        knight.protection += part["protection"]


def weapon_power(knight: Knights, weapon: dict) -> None:
    knight.power += weapon["power"]


def drink_potion(knight: Knights, potion: dict | None) -> None:
    if potion:
        for key, value in potion["effect"].items():
            knight.__dict__[key] += value


def preparation(
        knight: Knights,
        knight_dict: dict
) -> None:
    protection_calc(knight, knight_dict["armour"])
    weapon_power(knight, knight_dict["weapon"])
    drink_potion(knight, knight_dict["potion"])
