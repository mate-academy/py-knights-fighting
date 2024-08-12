from app.classes import Knight


def battle(knights_config: dict) -> dict:

    lancelot = Knight(
        "Lancelot",
        knights_config["lancelot"]["power"],
        knights_config["lancelot"]["hp"],
        knights_config["lancelot"]["armour"],
        knights_config["lancelot"]["weapon"],
        knights_config["lancelot"]["potion"]
    )

    arthur = Knight(
        "Arthur",
        knights_config["arthur"]["power"],
        knights_config["arthur"]["hp"],
        knights_config["arthur"]["armour"],
        knights_config["arthur"]["weapon"],
        knights_config["arthur"]["potion"]
    )

    mordred = Knight(
        "Mordred",
        knights_config["mordred"]["power"],
        knights_config["mordred"]["hp"],
        knights_config["mordred"]["armour"],
        knights_config["mordred"]["weapon"],
        knights_config["mordred"]["potion"]
    )

    red_knight = Knight(
        "Red Knight",
        knights_config["red_knight"]["power"],
        knights_config["red_knight"]["hp"],
        knights_config["red_knight"]["armour"],
        knights_config["red_knight"]["weapon"],
        knights_config["red_knight"]["potion"]
    )

    lancelot.final_hp -= max(
        0, mordred.final_power - lancelot.final_protection
    )
    mordred.final_hp -= max(
        0, lancelot.final_power - mordred.final_protection
    )

    arthur.final_hp -= max(
        0, red_knight.final_power - arthur.final_protection
    )
    red_knight.final_hp -= max(
        0, arthur.final_power - red_knight.final_protection
    )

    lancelot.final_hp = max(0, lancelot.final_hp)
    mordred.final_hp = max(0, mordred.final_hp)
    arthur.final_hp = max(0, arthur.final_hp)
    red_knight.final_hp = max(0, red_knight.final_hp)

    return {
        lancelot.name: lancelot.final_hp,
        arthur.name: arthur.final_hp,
        mordred.name: mordred.final_hp,
        red_knight.name: red_knight.final_hp,
    }
