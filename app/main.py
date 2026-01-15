from typing import Dict, Any
from app.knight import Knight
from app.battle import Battle
from app.knight_data import KNIGHTS


def battle(
        config: Dict[str, Any]
) -> Dict[str, int]:
    lancelot = Knight(**config["lancelot"])
    arthur = Knight(**config["arthur"])
    mordred = Knight(**config["mordred"])
    red_knight = Knight(**config["red_knight"])
    Battle.run_battle(lancelot, mordred)
    Battle.run_battle(arthur, red_knight)
    return Battle.get_battle_results(
        [lancelot,
         arthur,
         mordred,
         red_knight]
    )


print(battle(KNIGHTS))
