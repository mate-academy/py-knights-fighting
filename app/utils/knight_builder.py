from __future__ import annotations
from app.models.equipment import ArmourPiece, Weapon, Potion
from app.models.knight import Knight


class KnightBuilder:
    def __init__(self) -> None:
        pass

    def create_armour(self, armour_data: list) -> list:
        armour_pieces = []
        for armour_item in armour_data:
            armour_piece = ArmourPiece(
                part=armour_item["part"],
                protection=armour_item["protection"]
            )
            armour_pieces.append(armour_piece)
        return armour_pieces

    def create_weapon(self, weapon_data: dict) -> Weapon:
        return Weapon(
            name=weapon_data["name"],
            power=weapon_data["power"]
        )

    def create_knight(self, knight_key: str, config: dict) -> Knight:
        armour = self.create_armour(config.get("armour", []))
        weapon = self.create_weapon(config["weapon"])
        potion = Potion.create_from_dict(config.get("potion"))
        knight = Knight(
            name=config["name"],
            base_power=config["power"],
            base_hp=config["hp"],
            armour=armour,
            weapon=weapon,
            potion=potion
        )
        return knight

    def create_all_knights(self, knights_config: dict) -> dict:
        knights = {}
        for key, config in knights_config.items():
            knights[key] = self.create_knight(key, config)
        return knights
