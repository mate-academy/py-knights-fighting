from app.knights_data import KNIGHTS
from app.models import Knight
from app.battle import battle


def main() -> None:
    lancelot = Knight(KNIGHTS["lancelot"])
    mordred = Knight(KNIGHTS["mordred"])
    arthur = Knight(KNIGHTS["arthur"])
    red_knight = Knight(KNIGHTS["red_knight"])

    result1 = battle(lancelot, mordred)
    result2 = battle(arthur, red_knight)

    print(result1)
    print(result2)

if __name__ == "__main__":
    main()
