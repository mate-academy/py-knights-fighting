import os
import json

from app.knights.knight import Knight
from app.battles.battle import Battle


base_dir = os.path.dirname(__file__)
file_path = os.path.join(base_dir, "knights", "knights.json")

with open(file_path, "r") as file:
    knights = json.load(file)


def battle(knights_dict: dict) -> dict:
    rivals = {
        key: Knight(value)
        for key, value in knights_dict.items()
    }

    for knight in rivals.values():
        knight.get_ready()

    battles = [
        Battle(rivals["lancelot"], rivals["mordred"]),
        Battle(rivals["arthur"], rivals["red_knight"])
    ]

    return {
        knight: hp
        for fight in battles
        for knight, hp in fight.rumble().items()
    }


print(battle(knights))
