from __future__ import annotations

from app.characters.knight import Knight


def fight(fighters: list[Knight]) -> None:
    first_knight = fighters[0]
    second_knight = fighters[1]

    first_knight.strike(second_knight)
    second_knight.strike(first_knight)
