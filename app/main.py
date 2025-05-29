from typing import Dict

from app.models.armour import Armour
from app.models.knight import Knight
from app.models.potion import Potion
from app.models.weapon import Weapon
from app.services.battle import BattleService


def battle(knights_config: Dict[str, Dict]) -> Dict[str, int]:
    knights = {
        name: Knight(
            name=config["name"],
            power=config["power"],
            hp=config["hp"],
            weapon=Weapon(**config["weapon"]),
            armour=[Armour(**piece) for piece in config.get("armour", [])],
            potion=(
                Potion(**config["potion"])
                if config.get("potion")
                else None
            ),
        )
        for name, config in knights_config.items()
    }

    battle_pairs = [
        ("lancelot", "mordred"),
        ("arthur", "red_knight")
    ]

    results = {}

    for knight1_name, knight2_name in battle_pairs:
        knight1 = knights[knight1_name]
        knight2 = knights[knight2_name]

        knight1_stats = knight1.prepare_for_battle()
        knight2_stats = knight2.prepare_for_battle()

        knight1_result, knight2_result = BattleService.fight(
            knight1_stats,
            knight2_stats
        )

        results[knight1_result["name"]] = knight1_result["hp"]
        results[knight2_result["name"]] = knight2_result["hp"]

    expected_order = [k for k in results.keys()]
    ordered_results = {k: results[k] for k in expected_order}

    return ordered_results
