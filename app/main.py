from app.config.config import KNIGHTS
from app.knights.battle_preparation import Knight
from app.knights.battle import fight


def battle(knights_config: dict) -> dict:
    lancelot = Knight(**knights_config.get("lancelot"))
    arthur = Knight(**knights_config.get("arthur"))
    mordred = Knight(**knights_config.get("mordred"))
    red_knight = Knight(**knights_config.get("red_knight"))

    # 1 Lancelot vs Mordred:
    fight(lancelot, mordred)

    # 2 Arthur vs Red Knight:
    fight(arthur, red_knight)

    return {
        knights_config.get("lancelot").get("name"): lancelot.hp,
        knights_config.get("arthur").get("name"): arthur.hp,
        knights_config.get("mordred").get("name"): mordred.hp,
        knights_config.get("red_knight").get("name"): red_knight.hp,
    }


print(battle(KNIGHTS))
