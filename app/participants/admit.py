from __future__ import annotations

from app.participants.knight import Knight


def create_knights(knight_config: dict) -> Knight:
    knight = Knight(
        knight_config["name"],
        knight_config["power"],
        knight_config["hp"]
    )

    knight.attribute_counter(
        knight_config["armour"],
        knight_config["weapon"],
        knight_config["potion"]
    )

    return knight
