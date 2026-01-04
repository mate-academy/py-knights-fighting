from data.knights_data import KNIGHTS
from services.battle import battle

if __name__ == "__main__":
    results = battle(KNIGHTS)
    print(results)
