from typing import Any

from app.config.knights_config import KNIGHTS
from app.knights.factory import prepare_knight


def battle(knights_config: dict[str, Any]) -> dict[str, int]:
    lancelot = prepare_knight(knights_config["lancelot"])
    mordred = prepare_knight(knights_config["mordred"])
    arthur = prepare_knight(knights_config["arthur"])
    red_knight = prepare_knight(knights_config["red_knight"])

    lancelot.hp -= max(mordred.power - lancelot.protection, 0)
    mordred.hp -= max(lancelot.power - mordred.protection, 0)
    if lancelot.hp < 0:
        lancelot.hp = 0
    if mordred.hp < 0:
        mordred.hp = 0

    arthur.hp -= max(red_knight.power - arthur.protection, 0)
    red_knight.hp -= max(arthur.power - red_knight.protection, 0)
    if arthur.hp < 0:
        arthur.hp = 0
    if red_knight.hp < 0:
        red_knight.hp = 0

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


if __name__ == "__main__":
    print(battle(KNIGHTS))
