from app.attributes_of_knights.knights import Knight
from app.configs.lancelot_conf import lancelot_config


def prepare_lancelot() -> Knight:
    lancelot = Knight(
        name=lancelot_config["name"],
        power=lancelot_config["power"],
        hp=lancelot_config["hp"],
        armour=lancelot_config["armour"],
        weapon=lancelot_config["weapon"],
        potion=lancelot_config["potion"]
    )
    # apply armour
    lancelot.protection = lancelot.calculate_protection()

    # apply weapon
    lancelot.power = lancelot.calculate_power()

    # apply hp
    lancelot.hp = lancelot.calculate_hp()

    return lancelot
