from app.data.knights_data import KNIGHTS
from app.knights.factory import create_all_knights
from app.battles.battle import fight


def battle(knights_config: dict) -> dict:
    knights = create_all_knights(knights_config)

    for knight in knights.values():
        knight.prepare_for_battle()

    fight(knights["lancelot"], knights["mordred"])
    fight(knights["arthur"], knights["red_knight"])

    return {
        knight.name: knight.hp
        for knight in knights.values()
    }


if __name__ == "__main__":
    print(battle(KNIGHTS))
