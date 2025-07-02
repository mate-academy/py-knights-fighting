"""Battle mechanics for knights."""
from typing import Dict

from .knight import Knight


def create_knight(config: Dict) -> Knight:
    """Create a Knight instance from raw config."""
    return Knight(
        name=config["name"],
        base_power=config["power"],
        base_hp=config["hp"],
        armour=config.get("armour", []),
        weapon=config["weapon"],
        potion=config.get("potion"),
    )


def duel(left: Knight, right: Knight) -> None:
    """Make two knights exchange hits."""
    left.take_damage(right.power - left.protection)
    right.take_damage(left.power - right.protection)


def battle(config: Dict[str, Dict]) -> Dict[str, int]:
    """Run tournament and return hp of all knights."""
    knights = {name: create_knight(data) for name, data in config.items()}

    lancelot = knights["lancelot"]
    arthur = knights["arthur"]
    mordred = knights["mordred"]
    red_knight = knights["red_knight"]

    duel(lancelot, mordred)
    duel(arthur, red_knight)

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


__all__ = ["battle", "create_knight", "duel"]
