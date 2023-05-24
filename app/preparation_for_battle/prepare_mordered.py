from app.attributes_of_knights.knights import Knight
from app.configs.mordered_conf import mordred_config


def prepare_mordred() -> Knight:
    mordred = Knight(
        name=mordred_config["name"],
        power=mordred_config["power"],
        hp=mordred_config["hp"],
        armour=mordred_config["armour"],
        weapon=mordred_config["weapon"],
        potion=mordred_config["potion"]
    )
    # apply armour
    mordred.protection = mordred.calculate_protection()

    # apply weapon
    mordred.power = mordred.calculate_power()

    # apply hp
    mordred.hp = mordred.calculate_hp()

    return mordred
