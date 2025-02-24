from app.config import KNIGHTS
from app.battle import battle


def main() -> None:
    result = battle(KNIGHTS)
    print(result)


if __name__ == "__main__":
    main()
