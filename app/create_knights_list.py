import json
from typing import List

from app.knight import Knight


def create_knights_list(knights: json) -> List[Knight]:
    return [
        Knight(
            name=knights[knight]["name"],
            power=knights[knight]["power"],
            hp=knights[knight]["hp"],
            armour=knights[knight]["armour"]
            if len(knights[knight]["armour"]) > 0
            else None,
            weapon=knights[knight]["weapon"],
            potion=knights[knight]["potion"],
        )
        for knight in knights
    ]
