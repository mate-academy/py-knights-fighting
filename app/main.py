from app.knights.knights_config import KNIGHTS
from app.knights.battle_preparations import preparation
from app.knights.battle import fight, check_health


def battle(knights_config: dict) -> dict:

    # lancelot
    lancelot = knights_config["lancelot"]
    # arthur
    arthur = knights_config["arthur"]
    # mordred
    mordred = knights_config["mordred"]
    # red_knight
    red_knight = knights_config["red_knight"]

    # BATTLE PREPARATIONS:
    preparation(lancelot, arthur, mordred, red_knight)

    # BATTLE:
    # 1 Lancelot vs Mordred:
    fight(lancelot, mordred)

    # 2 Arthur vs Red Knight:
    fight(arthur, red_knight)

    # check if someone fell in battle
    check_health(lancelot, mordred, arthur, red_knight)

    # Return battle results:
    return {
        knight["name"]: knight["hp"]
        for knight in (lancelot, arthur, mordred, red_knight)
    }


print(battle(KNIGHTS))
