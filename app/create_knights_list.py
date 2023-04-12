from typing import List, Dict

from app.knight import Knight


def create_knights_list(knights: Dict[str, dict]) -> List[Knight]:
    return [
        Knight(
            name=knights[knight]["name"],
            power=knights[knight]["power"],
            hp=knights[knight]["hp"],
            armour=knights[knight]["armour"]
            if knights[knight]["armour"]
            else None,
            weapon=knights[knight]["weapon"],
            potion=knights[knight]["potion"],
        )
        for knight in knights
    ]
