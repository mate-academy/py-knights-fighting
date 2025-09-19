from app.knights.config import KNIGHTS
from app.battle.fight import battle


def main() -> None:
    print("🏰 Camelot Championship Begins! 🏰\n")
    results = battle(KNIGHTS)

    for knight, hp in results.items():
        print(f"{knight} → HP final: {hp}")


if __name__ == "__main__":
    main()
