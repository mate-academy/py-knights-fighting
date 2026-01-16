from typing import Dict
from app.battle.logic import fight
from app.knights.config import KNIGHTS
from app.knights.knight import Knight


def create_knights(names: list[str]) -> Dict[str, Knight]:
    return {name: Knight(KNIGHTS[name]) for name in names}


def main() -> None:
    knight_names = ["lancelot", "mordred", "arthur", "red_knight"]
    knights = create_knights(knight_names)

    battles = [("lancelot", "mordred"), ("arthur", "red_knight")]

    for i, (first, second) in enumerate(battles, 1):
        result = fight(knights[first], knights[second])
        print(f"Battle {i}: {knights[first].name} vs {knights[second].name}")
        print(result)


if __name__ == "__main__":
    main()
