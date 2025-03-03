from app.battle.fight import battle
from app.config.knights import KNIGHTS


if __name__ == "__main__":
    battle_results: dict[str, int] = battle(KNIGHTS)
    print(battle_results)
