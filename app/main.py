from config import get_knights_config
from battle import battle


def main() -> None:
    knights = get_knights_config()
    results = battle(knights)
    for name, hp in results.items():
        print(f"{name}: {hp} HP")


if __name__ == "__main__":
    main()
