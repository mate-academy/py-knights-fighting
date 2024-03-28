from app.functions import check_hp


def battle(knights_config: dict) -> dict:
    knights_list = []
    for i in knights_config.keys():
        knights_list.append(i)

    for kn in range(len(knights_list)):
        # BATTLE PREPARATIONS:
        knights_list[kn] = knights_config[knights_list[kn]]

        # apply armour
        knights_list[kn]["protection"] = 0
        for knight in knights_list[kn]["armour"]:
            knights_list[kn]["protection"] += knight["protection"]

        # apply weapon
        knights_list[kn]["power"] += knights_list[kn]["weapon"]["power"]

        # apply potion if exist
        if knights_list[kn]["potion"] is not None:
            if "power" in knights_list[kn]["potion"]["effect"]:
                knights_list[kn]["power"]\
                    += knights_list[kn]["potion"]["effect"]["power"]

            if "protection" in knights_list[kn]["potion"]["effect"]:
                knights_list[kn]["protection"]\
                    += knights_list[kn]["potion"]["effect"]["protection"]

            if "hp" in knights_list[kn]["potion"]["effect"]:
                knights_list[kn]["hp"]\
                    += knights_list[kn]["potion"]["effect"]["hp"]

    # BATTLE:
    lancelot = knights_list[0]
    arthur = knights_list[1]
    mordred = knights_list[2]
    red_knight = knights_list[3]

    # 1 Lancelot vs Mordred:
    lancelot["hp"] -= mordred["power"] - lancelot["protection"]
    mordred["hp"] -= lancelot["power"] - mordred["protection"]

    # check if someone fell in battle
    lancelot["hp"] = check_hp(lancelot["hp"])
    mordred["hp"] = check_hp(mordred["hp"])

    # 2 Arthur vs Red Knight:
    arthur["hp"] -= red_knight["power"] - arthur["protection"]
    red_knight["hp"] -= arthur["power"] - red_knight["protection"]

    # check if someone fell in battle
    arthur["hp"] = check_hp(arthur["hp"])
    red_knight["hp"] = check_hp(red_knight["hp"])

    # Return battle results:
    return {
        lancelot["name"]: lancelot["hp"],
        arthur["name"]: arthur["hp"],
        mordred["name"]: mordred["hp"],
        red_knight["name"]: red_knight["hp"],
    }
