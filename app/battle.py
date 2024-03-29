from app.functions import check_hp, apply_potion


def battle(knights_config: dict) -> dict:
    knights_list = [*knights_config.keys()]

    for kn in range(len(knights_list)):
        # BATTLE PREPARATIONS:
        knights_list[kn] = knights_config[knights_list[kn]]

        # apply potion
        apply_potion(knights_list, kn)

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
