from typing import Any


def knights_parameters(knight_name: Any) -> None:

    # Добавление брони рыцарю
    knight_name["protection"] = sum(
        a["protection"] for a in knight_name["armour"]
    )

    # Добавление оружия рыцарю
    knight_name["power"] += knight_name["weapon"]["power"]

    # Добавления зелья рыцарю, если оно есть
    if knight_name["potion"] is not None:
        if "power" in knight_name["potion"]["effect"]:
            knight_name["power"] += knight_name["potion"]["effect"]["power"]

        if "protection" in knight_name["potion"]["effect"]:
            protection_bonus = knight_name["potion"]["effect"]["protection"]
            knight_name["protection"] += protection_bonus

        if "hp" in knight_name["potion"]["effect"]:
            knight_name["hp"] += knight_name["potion"]["effect"]["hp"]


def battle_knight(first_knight: dict, second_knight: dict) -> None:
    first_knight["hp"] -= second_knight["power"] - first_knight["protection"]
    second_knight["hp"] -= first_knight["power"] - second_knight["protection"]

    if first_knight["hp"] <= 0:
        first_knight["hp"] = 0

    if second_knight["hp"] <= 0:
        second_knight["hp"] = 0
