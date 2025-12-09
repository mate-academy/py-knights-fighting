from app.Knights.data import KNIGHTS
from app.Knights.battle import battle


def main() -> None:
    result = battle(KNIGHTS)
    print(result)


if __name__ == "__main__":
    main()
