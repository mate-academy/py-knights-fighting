from app.data import data_objects
from app.knight import Knight, Battle


def create_knights(data_knights: dict) -> list:
    return [
        Knight(
            name=data_knight.get("name"),
            weapon=data_knight.get("weapon"),
            potion=data_knight.get("potion"),
            armour=data_knight.get("armour"),
            power=data_knight.get("power", 0),
            hp=data_knight.get("hp", 0)
        ) for data_knight in data_knights.values()
    ]


def battle(data_knights: dict) -> dict:
    battle_ = Battle(create_knights(data_knights))
    battle_.fight()
    return battle_.results_battle()


battle(data_objects.KNIGHTS)
