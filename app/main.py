from typing import Dict

from app.knight import Knight
from app.battle import Battle
from app.config import KNIGHTS


def battle(knights_config: Dict[str, Dict]) -> Dict[str, int]:
    knights = {
        name: Knight(**config)
        for name, config in knights_config.items()
    }
    results = {}

    battle_instance = Battle(knights["lancelot"], knights["mordred"])
    result = battle_instance.fight()
    results["Lancelot"] = result[knights["lancelot"].name]
    results["Mordred"] = result[knights["mordred"].name]

    battle_instance = Battle(knights["arthur"], knights["red_knight"])
    result = battle_instance.fight()
    results["Arthur"] = result[knights["arthur"].name]
    results["Red Knight"] = result[knights["red_knight"].name]

    return results


def main() -> None:
    result = battle(KNIGHTS)
    print(result)


if __name__ == "__main__":
    main()
