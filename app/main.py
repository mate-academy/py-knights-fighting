from app.knights import KNIGHTS
from app.equipment import apply_equipment
from app.combat import fight


def battle(knights_config: dict) -> dict:
    for knight in knights_config.values():
        apply_equipment(knight)

    fight(knights_config["lancelot"], knights_config["mordred"])
    fight(knights_config["arthur"], knights_config["red_knight"])

    return {
        knight["name"]: knight["hp"]
        for knight in knights_config.values()
    }


if __name__ == "__main__":
    print(battle(KNIGHTS))
