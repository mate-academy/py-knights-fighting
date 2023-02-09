from app.knight import Knight, KNIGHTS


def battle(knights_config: dict) -> dict:

    knights = dict()

    for name, stat in knights_config.items():
        knights[name] = Knight(stat)

    knights["lancelot"].duel(knights["mordred"])
    knights["arthur"].duel(knights["red_knight"])

    return {
        knights["lancelot"].name: knights["lancelot"].hp,
        knights["arthur"].name: knights["arthur"].hp,
        knights["mordred"].name: knights["mordred"].hp,
        knights["red_knight"].name: knights["red_knight"].hp,
    }


print(battle(KNIGHTS))
