from app.battle.logic import fight
from app.knights.config import KNIGHTS
from app.knights.knight import Knight


def main() -> None:
    lancelot = Knight(KNIGHTS["lancelot"])
    mordred = Knight(KNIGHTS["mordred"])
    arthur = Knight(KNIGHTS["arthur"])
    red_knight = Knight(KNIGHTS["red_knight"])

    result1 = fight(lancelot, mordred)
    result2 = fight(arthur, red_knight)

    print("Battle 1: Lancelot vs Mordred")
    print(result1)

    print("\nBattle 2: Arthur vs Red Knight")
    print(result2)


if __name__ == "__main__":
    main()
