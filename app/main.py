# main.py
from .battles import battle
from .knights import KNIGHTS

if __name__ == "__main__":
    battle_results = battle(KNIGHTS)
    print(battle_results)
