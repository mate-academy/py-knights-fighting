from app.attributes_of_knights.knights import Knight
from app.configs.arthur_conf import arthur_config


def prepare_arthur() -> Knight:
    arthur = Knight(
        name=arthur_config["name"],
        power=arthur_config["power"],
        hp=arthur_config["hp"],
        armour=arthur_config["armour"],
        weapon=arthur_config["weapon"],
        potion=arthur_config["potion"]
    )
    # apply armour
    arthur.protection = arthur.calculate_protection()

    # apply weapon
    arthur.power = arthur.calculate_power()

    # apply hp
    arthur.hp = arthur.calculate_hp()

    return arthur
