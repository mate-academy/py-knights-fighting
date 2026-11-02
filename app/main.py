from app.battle.battle import Battle
from app.data import KNIGHTS


def battle(knights_config: dict) -> dict:
    battle = Battle(knights_config)
    battle.pairs_fight()
    return battle.result()


if __name__ == "__main__":
    print(battle(KNIGHTS))
