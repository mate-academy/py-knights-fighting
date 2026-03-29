from app.knights.knights_data import KNIGHTS
from app.knights.battle import battle

if __name__ == "__main__":
    result = battle(KNIGHTS)
    print(result)
