from __future__ import annotations
from app.buttle.models import Knight, Weapon, Effect, Potion, Armour


def make_knights(knights_config: dict) -> list[Knight]:
    knights_instances = []

    for knight_name in knights_config:
        knight_dict = knights_config[knight_name]

        armours_list = []
        if knight_dict.get("armour"):
            armours_list = make_armour(
                knight_dict.get("armour"))

        weapon = Weapon(name=knight_dict["weapon"]["name"],
                        power=knight_dict["weapon"]["power"])

        potion = None
        if knight_dict.get("potion"):
            potion = make_potion(knight_dict.get("potion"))

        new_knight = Knight(name=knight_dict["name"],
                            power=knight_dict["power"],
                            hp=knight_dict["hp"],
                            armour=armours_list,
                            weapon=weapon,
                            potion=potion)
        new_knight.protection = 0

        if potion:
            new_knight.potion_bonus(potion)

        new_knight.calculate_protection()
        new_knight.calculate_power()
        knights_instances.append(new_knight)
    return knights_instances


def knights_to_dict(knights_instances: list[Knight]) -> dict:
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
