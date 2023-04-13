from typing import List, Dict

from app.knight import Knight


def create_knights_list(knights: Dict[str, dict]) -> List[Knight]:
    return [
        Knight(
            name=knight["name"],
            power=knight["power"],
            hp=knight["hp"],
            armour=knight["armour"]
            if knight["armour"]
            else None,
            weapon=knight["weapon"],
            potion=knight["potion"],
        )
        for knight in knights.values()
    ]
