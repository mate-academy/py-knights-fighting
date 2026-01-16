import json
from app.knight import Knight


def duel(rival1: Knight, rival2: Knight) -> dict:
    rival1.hp -= rival2.power - rival1.protection
    rival2.hp -= rival1.power - rival2.protection
    for rival in [rival1, rival2]:
        rival.hp = max(rival.hp, 0)
    return {rival1.name: rival1.hp, rival2.name: rival2.hp}


def battle(knights_config: dict) -> dict:
    knights = {name: Knight(knights_config[name]) for name in knights_config}
    return duel(
        knights["lancelot"],
        knights["mordred"]) | duel(knights["arthur"],
                                   knights["red_knight"]
                                   )


def load_knights_from_json(file_path: str) -> dict:
    with open(file_path, "r") as file:
        return json.load(file)


if __name__ == "__main__":
    knights_dict = load_knights_from_json("data.json")
    print(battle(knights_dict))
