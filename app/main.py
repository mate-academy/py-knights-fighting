from app.battles import battle
from knights_data import KNIGHTS

if __name__ == "__main__":
    battle_results = battle(KNIGHTS)
    print(battle_results)
