from app.knights_data import KNIGHTS
from app.battle import battle


if __name__ == "__main__":
    result = battle(KNIGHTS)
    print(result)
