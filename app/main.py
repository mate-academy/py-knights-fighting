from app.battle import battle
from app.knight_info import all_knights


if __name__ == "__main__":
    result = battle(all_knights)
    print(result)
