from app.battle.engine import battle
from app.config import KNIGHTS


def main() -> dict:
    return battle(KNIGHTS)


if __name__ == "__main__":
    print(main())
