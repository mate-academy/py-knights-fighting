from app.knights.knights_dict import KNIGHTS
from app.knights.knight import Knight


def battle(knights_config: dict) -> dict:
    knights = {}
    for name, knight in knights_config.items():
        knights[name] = Knight(knight)

    knights["lancelot"].battle(knights["mordred"])
    knights["arthur"].battle(knights["red_knight"])

    return {
        knights["lancelot"].name: knights["lancelot"].hp,
        knights["arthur"].name: knights["arthur"].hp,
        knights["mordred"].name: knights["mordred"].hp,
        knights["red_knight"].name: knights["red_knight"].hp
    }


print(battle(KNIGHTS))
