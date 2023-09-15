from __future__ import annotations
from app.data.knight_class import Knight


def create_knight(data: dict) -> Knight:
    knight = Knight(
        data["name"],
        data["power"],
        data["hp"]
    )

    knight.grab_weapon(data["weapon"])
    knight.suit_up(data["armour"])
    knight.drink_potion(data["potion"])

    return knight
