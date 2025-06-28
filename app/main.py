from .config import KNIGHTS
from .battle import battle, display_battle_results

if __name__ == "__main__":
    results = battle(KNIGHTS)
    display_battle_results(results)
