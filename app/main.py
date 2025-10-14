from typing import Dict, Any
from app.knights.knight import Knight
from app.battle.duel import simulate_duel


def battle(knights_config: Dict[str, Dict[str, Any]]) -> Dict[str, int]:
    lancelot = Knight(knights_config["lancelot"])
    mordred = Knight(knights_config["mordred"])
    arthur = Knight(knights_config["arthur"])
    red_knight = Knight(knights_config["red_knight"])

    simulate_duel(lancelot, mordred)
    simulate_duel(arthur, red_knight)

    results = {
        lancelot.name: lancelot.current_hp,
        mordred.name: mordred.current_hp,
        arthur.name: arthur.current_hp,
        red_knight.name: red_knight.current_hp,
    }

    return results


if __name__ == "__main__":
    from app.data.knights_data import KNIGHTS_CONFIG

    final_hp = battle(KNIGHTS_CONFIG)
    print(final_hp)
