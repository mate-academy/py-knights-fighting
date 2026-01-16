from models.knight import Knight
from services.battle import battle
from config import KNIGHTS


def main() -> None:
    lancelot = Knight(KNIGHTS["lancelot"])
    mordred = Knight(KNIGHTS["mordred"])
    arthur = Knight(KNIGHTS["arthur"])
    red_knight = Knight(KNIGHTS["red_knight"])

    battle1 = battle(lancelot, mordred)
    battle2 = battle(arthur, red_knight)

    print("Battle 1 results:")
    for name, hp in battle1.items():
        print(f"{name}: {hp} HP")

    print("\nBattle 2 results:")
    for name, hp in battle2.items():
        print(f"{name}: {hp} HP")


if __name__ == "__main__":
    main()
