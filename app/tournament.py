from typing import Any

from app.knight import Knight, Armour, Weapon, Potion


class BattleSetup:
    @staticmethod
    def enlist_knight(knight_config: dict[str, Any]) -> None:
        Knight(knight_config["name"], knight_config["power"],
               knight_config["hp"])

    @staticmethod
    def take_knight_to_armoury(knight_config: dict[str, Any]) -> None:
        # apply weapon
        knight = Knight.knights_enlisted[knight_config["name"]]
        knight.get_weapon(
            Weapon(
                knight_config["weapon"]["name"],
                knight_config["weapon"]["power"]
            )
        )

        # apply armour
        for armour_piece in knight_config["armour"]:
            knight.put_on_armour_piece(
                Armour(armour_piece["part"], armour_piece["protection"]))

        # apply potion if exist
        if knight_config.get("potion") is not None:
            knight.drink_potion(
                Potion(knight_config["potion"]["name"],
                       knight_config["potion"]["effect"].get("hp", 0),
                       knight_config["potion"]["effect"].get("power", 0),
                       knight_config["potion"]["effect"].get("protection", 0)))
