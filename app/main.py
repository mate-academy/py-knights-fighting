from app.configs import KNIGHTS
from app.battle import battle

if __name__ == "__main__":
    results = battle(KNIGHTS)
    print(results)
