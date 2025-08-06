from app.config import KNIGHTS
from app.battle import run_battle


if __name__ == "__main__":
    result = run_battle(KNIGHTS)
    print(result)
