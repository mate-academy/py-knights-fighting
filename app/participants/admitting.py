from __future__ import annotations

from app.participants.knights import Knights


def creating_knights(knight_config: dict) -> Knights:
    knight = Knights(
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
