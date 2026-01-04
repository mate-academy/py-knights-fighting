from app.battle import battle
from app.knights_data import knightsconfig


def main() -> None:
    result = battle(knightsconfig)
    print("Battle Result:")
    for knight, hp in result.items():
        print(f"{knight}: {hp} HP")


if __name__ == "__main__":
    main()
