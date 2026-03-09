from typing import Any, Dict
from app.knights.knight import Knight
from app.knights.armour import Armour
from app.knights.weapon import Weapon
from app.knights.potion import Potion
from app.battle.fight import fight


def create_knight(config: Dict[str, Any]) -> Knight:
    armour = [Armour(a["protection"]) for a in config.get("armour", [])]
    weapon = Weapon(config["weapon"]["power"])
    potion = (
        Potion(config["potion"]["effect"])
        if config.get("potion")
        else None
    )

    return Knight(
        name=config["name"],
        hp=config["hp"],
        power=config["power"],
        armour=armour,
        weapon=weapon,
        potion=potion,
    )


def battle(knights_config: dict) -> dict:
    knights = {
        name: create_knight(config)
        for name, config in knights_config.items()
    }

    fight(knights["lancelot"], knights["mordred"])
    fight(knights["arthur"], knights["red_knight"])

    return {
        knight.name: knight.hp
        for knight in knights.values()
    }
