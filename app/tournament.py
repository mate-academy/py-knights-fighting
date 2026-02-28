from typing import Any

from app.knight import Knight, Armour, Weapon, Potion


class Lists:
    @staticmethod
    def enlist_knight(knight: dict[str, Any]) -> None:
        Knight(knight["name"], knight["power"], knight["hp"])

    @staticmethod
    def take_knight_to_armoury(knight: dict[str, Any]) -> None:
        # apply weapon
        Knight.knights_enlisted[knight["name"]].get_weapon(
            Weapon(knight["weapon"]["name"], knight["weapon"]["power"])
        )

        # apply armour
        for armour_piece in knight["armour"]:
            Knight.knights_enlisted[knight["name"]].put_on_armour_piece(
                Armour(armour_piece["part"], armour_piece["protection"]))

        # apply potion if exist
        if knight.get("potion") is not None:
            Knight.knights_enlisted[knight["name"]].drink_potion(
                Potion(knight["potion"]["name"],
                       knight["potion"]["effect"].get("hp", 0),
                       knight["potion"]["effect"].get("power", 0),
                       knight["potion"]["effect"].get("protection", 0)))
