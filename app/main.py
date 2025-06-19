from typing import Dict, Any
from app.knights.knight import Knight
from app.knights.armour import Armour
from app.knights.weapon import Weapon
from app.knights.potion import Potion
from app.battle.simulator import simulate_battle


def parse_knight(data: Dict[str, Any]) -> Knight:
    armours = [
        Armour(part=a["part"], protection=a["protection"])
        for a in data.get("armour", [])
    ]
    weapon = Weapon(**data["weapon"])
    potion_data = data.get("potion")
    potion = Potion(**potion_data) if potion_data else None

    return Knight(
        name=data["name"],
        base_power=data["power"],
        base_hp=data["hp"],
        armour=armours,
        weapon=weapon,
        potion=potion,
    )


def battle(config: Dict[str, Dict[str, Any]]) -> Dict[str, int]:
    required_knights = {"lancelot", "mordred", "arthur", "red_knight"}
    missing = required_knights - config.keys()
    if missing:
        raise KeyError(
            f"Missing knight(s) in config: {", ".join(missing)}"
        )

    knights = {name: parse_knight(config[name]) for name in required_knights}

    result1 = simulate_battle(knights["lancelot"], knights["mordred"])
    result2 = simulate_battle(knights["arthur"], knights["red_knight"])

    return {**result1, **result2}
