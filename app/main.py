
from app.models.knights import KNIGHTS
from app.battle.fight import battle


def main() -> int:
    results = battle(KNIGHTS)

    print("=== BATTLE RESULTS ===")

    for knight, hp in results.items():
        print(f"{knight}: {hp} HP")


if __name__ == "__main__":
    main()
