from dataclasses import dataclass
from app.battle_preparations.load_from_file import to_create_knight


@dataclass
class Knight:
    name: str
    power: int
    hp: int
    protection: int = 0


def ready_knights(knights_dict: dict) -> list:
    knights = to_create_knight(knights_dict)
    return [
        Knight(
            name=knight["name"],
            power=knight["power"],
            hp=knight["hp"]
        )
        for knight in knights
    ]
