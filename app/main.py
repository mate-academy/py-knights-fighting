from app.knights.knights_characters import Knights


def preparing(knights_config: dict) -> dict:

    # BATTLE PREPARATIONS:
    for temp_knight in knights_config:
        index = 0

        # apply armour
        knights_config[temp_knight]["protection"] = 0
        for a in knights_config[temp_knight]["armour"]:
            knights_config[temp_knight]["protection"] += a["protection"]

        # apply weapon
        knights_config[temp_knight]["power"] += knights_config[temp_knight]["weapon"]["power"]

        # apply potion if exist
        if knights_config[temp_knight]["potion"] is not None:
            if "power" in knights_config[temp_knight]["potion"]["effect"]:
                knights_config[temp_knight]["power"] += knights_config[temp_knight]["potion"]["effect"]["power"]

            if "protection" in knights_config[temp_knight]["potion"]["effect"]:
                knights_config[temp_knight]["protection"] += knights_config[temp_knight]["potion"]["effect"]["protection"]

            if "hp" in knights_config[temp_knight]["potion"]["effect"]:
                knights_config[temp_knight]["hp"] += knights_config[temp_knight]["potion"]["effect"]["hp"]
            index += 1
    return knights_config


def battle(knights_config: dict):

    knights_config = preparing(knights_config)
    print(knights_config)

    # BATTLE:
    # 1 Lancelot vs Mordred:
    knights_config["lancelot"]["hp"] -= knights_config["mordred"]["power"] - knights_config["lancelot"]["protection"]
    knights_config["mordred"]["hp"] -= knights_config["mordred"]["power"] - knights_config["mordred"]["protection"]

    # check if someone fell in battle
    if knights_config["lancelot"]["hp"] <= 0:
        knights_config["lancelot"]["hp"] = 0

    if knights_config["mordred"]["hp"] <= 0:
        knights_config["mordred"]["hp"] = 0

    # 2 Arthur vs Red Knight:
    knights_config["arthur"]["hp"] -= knights_config["red_knight"]["power"] - knights_config["arthur"]["protection"]
    knights_config["red_knight"]["hp"] -= knights_config["arthur"]["power"] - knights_config["red_knight"]["protection"]

    # check if someone fell in battle
    if knights_config["arthur"]["hp"] <= 0:
        knights_config["arthur"]["hp"] = 0

    if knights_config["red_knight"]["hp"] <= 0:
        knights_config["red_knight"]["hp"] = 0

    # Return battle results:
    return {
        knights_config["lancelot"]["name"]: knights_config["lancelot"]["hp"],
        knights_config["arthur"]["name"]: knights_config["arthur"]["hp"],
        knights_config["mordred"]["name"]: knights_config["mordred"]["hp"],
        knights_config["red_knight"]["name"]: knights_config["red_knight"]["hp"],
    }


print(battle(Knights.KNIGHTS))
