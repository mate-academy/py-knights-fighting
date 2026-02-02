from app.characters.knights import Knight
from app.equipment.armour import Armour
from app.equipment.weapon import Weapon
from app.equipment.potion import Potion
from app.game.battle import fight, results


def battle(knights_config: dict) -> dict:
    knights: dict[str, Knight] = {}

    for key, cfg in knights_config.items():
        weapon_cfg = cfg["weapon"]
        weapon = Weapon(name=weapon_cfg["name"], power=weapon_cfg["power"])

        potion_cfg = cfg.get("potion")
        potion = None
        if potion_cfg is not None:
            potion = Potion(name=potion_cfg["name"],
                            effect=potion_cfg["effect"])

        armour_dict: dict[str, Armour] = {}
        for item in cfg.get("armour", []):
            part = item["part"]
            armour_dict[part] = Armour(part=part,
                                       protection=item["protection"])

        knights[key] = Knight(
            name=cfg["name"],
            hp=cfg["hp"],
            power=cfg["power"],
            weapon=weapon,
            potion=potion,
            armour=armour_dict,
        )

    fight(knights["lancelot"], knights["mordred"])
    fight(knights["arthur"], knights["red_knight"])

    return results(
        knights["lancelot"],
        knights["arthur"],
        knights["mordred"],
        knights["red_knight"],
    )
