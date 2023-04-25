from app.battle_preparations import get_equipment
from app.battle import fight


def battle(knights_config: dict) -> dict:
    for knight_name, knight_data in knights_config.items():
        get_equipment(knight_data)

    fights = [("lancelot", "mordred"), ("arthur", "red_knight")]
    for knight1_name, knight2_name in fights:
        knight1 = knights_config[knight1_name]
        knight2 = knights_config[knight2_name]
        fight(knight1, knight2)

    return {
        knight["name"]: knight["hp"] for knight in knights_config.values()
    }
