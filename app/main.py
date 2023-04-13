import json
import os
from typing import Dict, Any

from app.fight import fight
from app.create_knights_list import create_knights_list
from app.calculate_knights_stats import calculate_knights_stats


def battle(kingdom_knights: Dict[str, Any]) -> Dict[str, int]:
    knights_list = create_knights_list(kingdom_knights)

    calculate_knights_stats(knights_list)

    knights_dict = {knight.name: knight for knight in knights_list}

    lancelot = knights_dict.get("Lancelot")
    artur = knights_dict.get("Artur")
    mordred = knights_dict.get("Mordred")
    red_knight = knights_dict.get("Red Knight")

    fight(lancelot, mordred)
    fight(artur, red_knight)

    return {
        lancelot.name: lancelot.hp,
        artur.name: artur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


if __name__ == "__main__":
    path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "config.json"
    )

    with open(path, "r") as data:
        knights = json.load(data)
        print(battle(kingdom_knights=knights))
