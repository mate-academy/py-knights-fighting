from typing import Dict
from app.knight import Knight


def create_knights(config: Dict[str, dict]) -> Dict[str, Knight]:
    knights = {}
    for key, data in config.items():
        knights[key] = Knight(
            name=data["name"],
            hp=data["hp"],
            power=data["power"],
            armour=data["armour"],
            weapon=data["weapon"],
            potion=data.get("potion")
        )
    return knights


def battle(knights_dict: Dict[str, dict]) -> Dict[str, int]:
    knights = create_knights(knights_dict)

    for knight in knights.values():
        knight.prepare_for_battle()

    battles = [("lancelot", "mordred"), ("arthur", "red_knight")]

    results = {}
    for first, second in battles:
        first_knight = knights[first]
        second_knight = knights[second]

        first_knight_hp = max(
            0, first_knight.hp - (second_knight.power - first_knight.protection)
        )
        second_knight_hp = max(
            0, second_knight.hp - (first_knight.power - second_knight.protection)
        )

        results[first_knight.name] = first_knight_hp
        results[second_knight.name] = second_knight_hp

    return results
