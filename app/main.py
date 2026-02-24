from app.battle_logic.battle import battle
from app.solution.parametrs_knights import KNIGHTS


if __name__ == "__main__":
    result = battle(KNIGHTS)
    print(result)
