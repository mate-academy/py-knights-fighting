from app.constants import KNIGHTS
from app.factories import get_knights

from app.utils import fight


def battle(knights_config: dict) -> dict:
    # BATTLE PREPARATIONS:

    knights = get_knights(knights_config)

    # BATTLE:

    # 1 Lancelot vs Mordred:
    fight(knights["lancelot"], knights["mordred"])

    # 2 Arthur vs Red Knight:
    fight(knights["arthur"], knights["red_knight"])

    # Return battle results:
    return {
        knights["lancelot"].name: knights["lancelot"].hp,
        knights["arthur"].name: knights["arthur"].hp,
        knights["mordred"].name: knights["mordred"].hp,
        knights["red_knight"].name: knights["red_knight"].hp,
    }


print(battle(KNIGHTS))
