from app.constants import KNIGHTS
from app.factories.game_knight_factory import GameKnightFactory
from app.models.knight import KnightDict, KnightName


def battle(knights_config: KnightDict) -> dict[str, int]:
    knights: dict[KnightName, GameKnightFactory] = {}

    for knight_name, knight_data in knights_config.items():
        knights[knight_name] = GameKnightFactory(knight_data)

    # -------------------------------------------------------------------------------
    # BATTLE:

    knights["lancelot"].battle_with(knights["mordred"])
    knights["arthur"].battle_with(knights["red_knight"])

    # Return battle results:
    return {
        knights["lancelot"].name: knights["lancelot"].hp,
        knights["arthur"].name: knights["arthur"].hp,
        knights["mordred"].name: knights["mordred"].hp,
        knights["red_knight"].name: knights["red_knight"].hp,
    }


print(battle(KNIGHTS))
