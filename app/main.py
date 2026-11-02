from app.battle.battle import Battle
from app.data import KNIGHTS


def battle(knights_config: dict) -> dict:
    battle_instance = Battle(knights_config)
    battle_instance.pairs_fight()
    return battle_instance.result()


if __name__ == "__main__":
    print(battle(KNIGHTS))
