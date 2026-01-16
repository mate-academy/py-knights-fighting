from app.knight import Knight
from app.battle import battle_two_knights
from app.mock_data import KNIGHTS


def battle(knights_config: dict) -> dict[str, int]:

    lancelot = Knight(knights_config["lancelot"])
    arthur = Knight(knights_config["arthur"])
    mordred = Knight(knights_config["mordred"])
    red_knight = Knight(knights_config["red_knight"])

    result1 = battle_two_knights(lancelot, mordred)
    result2 = battle_two_knights(arthur, red_knight)

    return {
        **result1,
        **result2,
    }


print(battle(KNIGHTS))
