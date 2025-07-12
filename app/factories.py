from app.armour import Armour
from app.knight import Knight
from app.potion import Potion
from app.weapon import Weapon


def get_armour(armour_list: list) -> Armour:
    armour = Armour(0, [])
    for part in armour_list:
        armour.protection += part.get("protection", 0)
        armour.parts.append(part.get("part"))
    return armour


def get_weapon(weapon: dict) -> Weapon:
    return Weapon(weapon.get("name"), weapon.get("power"))


def get_potion(potion: dict) -> Potion:
    if potion:
        name = potion.get("name")
        effect = potion.get("effect", {})
        hp = effect.get("hp", 0)
        power = effect.get("power", 0)
        protection = effect.get("protection", 0)
        return Potion(name, hp, power, protection)
    return Potion("None", 0, 0, 0)


def get_knights(knights_config: dict) -> dict:
    lancelot = Knight(
        name=knights_config["lancelot"]["name"],
        hp=knights_config["lancelot"]["hp"],
        power=knights_config["lancelot"]["power"],
        armour=get_armour(knights_config["lancelot"].get("armour", [])),
        weapon=get_weapon(knights_config["lancelot"]["weapon"]),
        potion=get_potion(knights_config["lancelot"].get("potion", {}))
    )

    arthur = Knight(
        name=knights_config["arthur"]["name"],
        hp=knights_config["arthur"]["hp"],
        power=knights_config["arthur"]["power"],
        armour=get_armour(knights_config["arthur"].get("armour", [])),
        weapon=get_weapon(knights_config["arthur"]["weapon"]),
        potion=get_potion(knights_config["arthur"].get("potion", {}))
    )

    mordred = Knight(
        name=knights_config["mordred"]["name"],
        hp=knights_config["mordred"]["hp"],
        power=knights_config["mordred"]["power"],
        armour=get_armour(knights_config["mordred"].get("armour", [])),
        weapon=get_weapon(knights_config["mordred"]["weapon"]),
        potion=get_potion(knights_config["mordred"].get("potion", {}))
    )

    red_knight = Knight(
        name=knights_config["red_knight"]["name"],
        hp=knights_config["red_knight"]["hp"],
        power=knights_config["red_knight"]["power"],
        armour=get_armour(knights_config["red_knight"].get("armour", [])),
        weapon=get_weapon(knights_config["red_knight"]["weapon"]),
        potion=get_potion(knights_config["red_knight"].get("potion", {}))
    )

    return {
        "lancelot": lancelot,
        "arthur": arthur,
        "mordred": mordred,
        "red_knight": red_knight
    }
