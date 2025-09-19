from app.knights.config import KNIGHTS
from app.battle.fight import battle


def main() -> None:
    print("🏰 Camelot Championship Begins! 🏰\n")
    winner1 = battle(KNIGHTS["Lancelot"], KNIGHTS["Mordred"])
    print(f"Lancelot vs Mordred → Winner: {winner1}")
    winner2 = battle(KNIGHTS["Arthur"], KNIGHTS["Red Knight"])
    print(f"Arthur vs Red Knight → Winner: {winner2}")


if __name__ == "__main__":
    main()
