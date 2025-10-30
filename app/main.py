from typing import Dict
from app.fight.prebattle import prepare_all_knights
from app.fight.battle import conduct_battle


def battle(knights_config: Dict) -> Dict[str, int]:

    # 1. PREPARATION: ready-to-fight Knight objects.
    prepared_knights = prepare_all_knights(knights_config)

    # 2. Retrieve the specific knights for the scheduled battles.
    lancelot = prepared_knights["lancelot"]
    mordred = prepared_knights["mordred"]
    arthur = prepared_knights["arthur"]
    red_knight = prepared_knights["red_knight"]

    # 3. COMBAT EXECUTION: Execute the two scheduled battles.
    # Lancelot vs Mordred
    conduct_battle(lancelot, mordred)

    # Arthur vs Red Knight
    conduct_battle(arthur, red_knight)

    # 4. RESULTS: Return the final HP state of all combatants.
    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }
