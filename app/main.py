from typing import Dict
from configs import KNIGHTS
from knight import Knight
from battle import battle


def create_knights(knight_data: Dict) -> Knight:
    return Knight(
        name=knight_data["name"],
        power=knight_data["power"],
        hp=knight_data["hp"],
        armour=knight_data.get("armour", []),
        weapon=knight_data.get("weapon"),
        potion=knight_data.get("potion"),
    )


def main() -> None:
    lancelot = create_knights(KNIGHTS["lancelot"])
    arthur = create_knights(KNIGHTS["arthur"])
    mordred = create_knights(KNIGHTS["mordred"])
    red_knight = create_knights(KNIGHTS["red_knight"])

    print("Battle 1: Lancelot vs Mordred")
    result1 = battle(lancelot, mordred)
    print(result1)

    print("Battle 2: Arthur vs Red Knight")
    result2 = battle(arthur, red_knight)
    print(result2)


if __name__ == "__main__":
    main()
