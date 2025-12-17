from app.constants import KNIGHTS
from app.factories.game_knight_factory import GameKnightFactory
from app.models.knight import KnightDict


def battle(knights_config: KnightDict) -> dict[str, int]:
    # BATTLE PREPARATIONS:
    lancelot = GameKnightFactory(knights_config["lancelot"])
    arthur = GameKnightFactory(knights_config["arthur"])
    mordred = GameKnightFactory(knights_config["mordred"])
    red_knight = GameKnightFactory(knights_config["red_knight"])

    # -------------------------------------------------------------------------------
    # BATTLE:

    lancelot.battle_with(mordred)
    arthur.battle_with(red_knight)

    # Return battle results:
    return {
        lancelot["name"]: lancelot["hp"],
        arthur["name"]: arthur["hp"],
        mordred["name"]: mordred["hp"],
        red_knight["name"]: red_knight["hp"],
    }


print(battle(KNIGHTS))
