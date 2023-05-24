from app.attributes_of_knights.knights import Knight
from app.configs.red_knight_conf import red_knight_config


def prepare_red_knight() -> Knight:
    red_knight = Knight(
        name=red_knight_config["name"],
        power=red_knight_config["power"],
        hp=red_knight_config["hp"],
        armour=red_knight_config["armour"],
        weapon=red_knight_config["weapon"],
        potion=red_knight_config["potion"]
    )
    # apply armour
    red_knight.protection = red_knight.calculate_protection()

    # apply weapon
    red_knight.power = red_knight.calculate_power()

    # apply hp
    red_knight.hp = red_knight.calculate_hp()

    return red_knight
