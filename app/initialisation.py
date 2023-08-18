"""
This module configures Knight instances.
"""
from app.knight import Knight


def prepare_for_battle(knight: dict) -> Knight:
    name = knight["name"]
    characteristics = {
        "power": knight["power"] + knight["weapon"]["power"],
        "hp": knight["hp"],
        "protection": 0
    }
    bonus = check_for_perks(knight)
    for char, value in bonus.items():
        characteristics[char] += value
    return Knight(
        name,
        characteristics["power"],
        characteristics["hp"],
        characteristics["protection"]
    )


def check_for_perks(knight: dict) -> dict:
    bonus = {
        "power": 0,
        "protection": 0,
        "hp": 0
    }
    for armour_piece in knight["armour"]:
        bonus["protection"] += armour_piece["protection"]
    if knight["potion"] is not None:
        for char, value in knight["potion"]["effect"].items():
            bonus[char] += value
    return bonus
