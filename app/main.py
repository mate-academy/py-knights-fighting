from app.knights import Knight
from app.knights_config import KNIGHTS
from app.preparation_and_battle import apply_preparation
from app.preparation_and_battle import battle


def create_knights(knights: dict) -> dict:
    knight_instances = {}

    for knight_name, knight_value in KNIGHTS.items():
        knight_instance = Knight(
            name=knight_value["name"],
            power=knight_value["power"],
            hp=knight_value["hp"],
            armour=knight_value["armour"],
            weapon=knight_value["weapon"],
            potion=knight_value["potion"],
        )
        knight_instances[knight_name] = knight_instance
    return knight_instances


knight_instances = create_knights(KNIGHTS)

apply_preparation(knight_instances)

battle_result_hp = battle(knight_instances)

print(battle_result_hp)
