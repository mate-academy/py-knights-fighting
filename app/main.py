from typing import Dict, Any, Tuple
from app.knights import Knight
from app.battle import Battle
from app.data import KNIGHTS


def setup_knights(config: Dict[str, Any]) -> (
        Tuple)[Knight, Knight, Knight, Knight]:
    lancelot = Knight(**config["lancelot"])
    arthur = Knight(**config["arthur"])
    mordred = Knight(**config["mordred"])
    red_knight = Knight(**config["red_knight"])

    lancelot.apply_potion()
    arthur.apply_potion()
    mordred.apply_potion()
    red_knight.apply_potion()

    return lancelot, arthur, mordred, red_knight


def battle(knights_config: Dict[str, Any]) -> Dict[str, int]:
    lancelot, arthur, mordred, red_knight = setup_knights(knights_config)

    battle1 = Battle(lancelot, mordred)
    result1 = battle1.fight()

    battle2 = Battle(arthur, red_knight)
    result2 = battle2.fight()

    return {**result1, **result2}


print(battle(KNIGHTS))
