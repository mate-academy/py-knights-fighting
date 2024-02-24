from app.helpers.types import NewKnightsConfig
from app.heroes.knight import Knight
from app.equipment.knight import Weapon


def transform_to_new_knights_config(old_knights_config: dict) -> NewKnightsConfig:
    new_config = []

    for old_knight in old_knights_config:
        old_weapon = old_knight["weapon"]
        new_config.append(
            Knight(
                name=old_knight["name"],
                power=old_knight["power"],
                hp=old_knight["hp"],
                armour=old_knight["armour"],
                weapon=Weapon(
                    name=old_weapon["name"],
                    power=old_weapon["power"]
                )
            )
        )
