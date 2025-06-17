from app.config import knights_data
from app.battle.mechanics import prepare_knights, fight


def battle(knights_config: dict = knights_data) -> dict:
    knights = prepare_knights(knights_config)
    fight(knights["lancelot"], knights["mordred"])
    fight(knights["arthur"], knights["red_knight"])
    return {
        knights["lancelot"].name: knights["lancelot"].hp,
        knights["arthur"].name: knights["arthur"].hp,
        knights["mordred"].name: knights["mordred"].hp,
        knights["red_knight"].name: knights["red_knight"].hp,
    }


print(battle(knights_data))
