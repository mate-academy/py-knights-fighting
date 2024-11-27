from typing import Dict, Any
from app.knights.knight import Knight


def battle(knights_config: Dict[str, Dict[str, Any]]) -> Dict[str, int]:
    try:
        knights = {
            name: Knight(**data)
            for name, data in knights_config.items()}
    except KeyError as e:
        raise ValueError(f"Missing expected knight data for {str(e)}")

    lancelot = knights.get("lancelot")
    mordred = knights.get("mordred")
    arthur = knights.get("arthur")
    red_knight = knights.get("red_knight")

    if not all([lancelot, mordred, arthur, red_knight]):
        raise ValueError(
            "One or more knights are missing in the configuration."
        )

    lancelot_hp = (lancelot.get_effective_hp()
                   - max(mordred.get_effective_power()
                         - lancelot.get_effective_protection(),
                         0)
                   )
    mordred_hp = (mordred.get_effective_hp()
                  - max(lancelot.get_effective_power()
                        - mordred.get_effective_protection(),
                        0))

    arthur_hp = (arthur.get_effective_hp()
                 - max(red_knight.get_effective_power()
                       - arthur.get_effective_protection(),
                       0))
    red_knight_hp = (red_knight.get_effective_hp()
                     - max(arthur.get_effective_power()
                           - red_knight.get_effective_protection(),
                           0))

    return {
        "Lancelot": max(lancelot_hp, 0),
        "Arthur": max(arthur_hp, 0),
        "Mordred": max(mordred_hp, 0),
        "Red Knight": max(red_knight_hp, 0),
    }
