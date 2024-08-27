from app.battle import battle
from app.knights_conf import KNIGHTS


if __name__ == "__main__":
    result = battle(KNIGHTS)
    print(result)
