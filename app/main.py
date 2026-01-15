from app.knight_config import KNIGHTS
from app.battle import Battle


def battle(knights: dict) -> dict:
    battle_instance = Battle(knights)
    battle_instance.fight()
    return battle_instance.get_results()


if __name__ == "__main__":
    results = battle(KNIGHTS)
    print(results)
