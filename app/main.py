from app.battle.battle import Battle
from app.prepare_to_battle.knight_is_ready import IsReady
from app.knights_dict import KNIGHTS


def battle(knights_config: dict) -> str:

    lancelot = IsReady(knights_config["lancelot"]).is_ready()
    arthur = IsReady(knights_config["arthur"]).is_ready()
    mordred = IsReady(knights_config["mordred"]).is_ready()
    red_knight = IsReady(knights_config["red_knight"]).is_ready()

    first_battle = Battle(lancelot, mordred)
    first_battle.fight()
    second_battle = Battle(arthur, red_knight)
    second_battle.fight()
    return Battle.battles_result


print(battle(KNIGHTS))
