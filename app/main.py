from app.battle.battle import tournament
from app.data.knights_data import KNIGHTS


def battle(knights_config: dict) -> dict:
    return tournament(knights_config)


if __name__ == "__main__":
    result = battle(KNIGHTS)
    print(result)
