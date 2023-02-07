from __future__ import annotations
from app.buttle.preparations_classes import Knight, Weapon, Effect, Potion, \
    Armour


def list_of_knight_instances_from_dict(knights_config: dict) -> list[Knight]:
    knights_instances = []
    for knight_name in knights_config:

        # armour

        armours_list = []
        if knights_config[knight_name].get("armour"):
            armours_list = make_armour(
                knights_config[knight_name].get("armour"))

        # weapon
        weapon = Weapon(name=knights_config[knight_name]["weapon"]["name"],
                        power=knights_config[knight_name]["weapon"]["power"])
        # potion
        potion = None
        if knights_config[knight_name].get("potion"):
            # effect
            potion = make_potion(knights_config[knight_name].get("potion"))

        new_knight = Knight(name=knights_config[knight_name]["name"],
                            power=knights_config[knight_name]["power"],
                            hp=knights_config[knight_name]["hp"],
                            armour=armours_list, weapon=weapon, potion=potion)
        new_knight.protection = 0

        if potion:
            potion_bonus(new_knight, potion)

        for armour in new_knight.armour:
            new_knight.protection += armour.protection

        new_knight.power += new_knight.weapon.power

        knights_instances.append(new_knight)
    return knights_instances


def list_of_knights_to_dict(knights_instances: list[Knight]) -> dict:
    return {
        knights_instances[0].name: knights_instances[0].hp,
        knights_instances[1].name: knights_instances[1].hp,
        knights_instances[2].name: knights_instances[2].hp,
        knights_instances[3].name: knights_instances[3].hp,
    }


def make_armour(armour_for_knight: list[dict]) -> list[Armour]:
    armours_list = []
    for armour in armour_for_knight:
        new_armour = Armour(part=armour["part"],
                            protection=armour["protection"])
        armours_list.append(new_armour)
    return armours_list


def make_potion(potion_dict: dict) -> Potion:
    effect = Effect(hp=potion_dict["effect"]["hp"],
                    power=potion_dict["effect"]["power"],
                    protection=potion_dict["effect"].get("protection"))

    potion = Potion(name=potion_dict["name"],
                    effect=effect)

    return potion


def potion_bonus(knight: Knight, potion: Potion) -> None:
    if potion.effect.power:
        knight.power += knight.potion.effect.power
    if potion.effect.protection:
        knight.protection += knight.potion.effect.protection
    if potion.effect.hp:
        knight.hp += knight.potion.effect.hp
