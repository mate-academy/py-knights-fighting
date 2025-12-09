from typing import Any

from app.config.knights_config import KNIGHTS
from app.knights.battle import battle as perform_battle
from app.knights.factory import prepare_knight


def battle(knights_config: dict[str, Any]) -> dict[str, int]:
    lancelot = prepare_knight(knights_config["lancelot"])
    mordred = prepare_knight(knights_config["mordred"])
    arthur = prepare_knight(knights_config["arthur"])
    red_knight = prepare_knight(knights_config["red_knight"])

    perform_battle(lancelot, mordred)
    perform_battle(arthur, red_knight)

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


if __name__ == "__main__":
    print(battle(KNIGHTS))
