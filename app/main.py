from app.knights.lancelot import lancelot
from app.knights.arthur import arthur
from app.knights.mordred import mordred
from app.knights.red_knight import red_knight
from app.battle_test.preparation import Preparation


KNIGHTS = {
    "lancelot": lancelot(),
    "arthur": arthur(),
    "mordred": mordred(),
    "red_knight": red_knight()
}


def battle(knightsConfig) -> dict:
    # BATTLE PREPARATIONS:

    # lancelot
    lancelot = Preparation(knightsConfig["lancelot"])

    # apply armour
    # lancelot["protection"] = 0
    # for a in lancelot["armour"]:
    #     lancelot["protection"] += a["protection"]
    #
    # # apply weapon
    # lancelot["power"] += lancelot["weapon"]["power"]
    #
    # # apply potion if exist
    # if lancelot["potion"] is not None:
    #     if "power" in lancelot["potion"]["effect"]:
    #         lancelot["power"] += lancelot["potion"]["effect"]["power"]
    #
    #     if "protection" in lancelot["potion"]["effect"]:
    #         lancelot["protection"] += lancelot["potion"]["effect"]["protection"]
    #
    #     if "hp" in lancelot["potion"]["effect"]:
    #         lancelot["hp"] += lancelot["potion"]["effect"]["hp"]

    # arthur.knight
    arthur = Preparation(knightsConfig["arthur"])

    # # apply armour
    # arthur.knight["protection"] = 0
    # for a in arthur.knight["armour"]:
    #     arthur.knight["protection"] += a["protection"]
    #
    # # apply weapon
    # arthur.knight["power"] += arthur.knight["weapon"]["power"]
    #
    # # apply potion if exist
    # if arthur.knight["potion"] is not None:
    #     if "power" in arthur.knight["potion"]["effect"]:
    #         arthur.knight["power"] += arthur.knight["potion"]["effect"]["power"]
    #
    #     if "protection" in arthur.knight["potion"]["effect"]:
    #         arthur.knight["protection"] += arthur.knight["potion"]["effect"]["protection"]
    #
    #     if "hp" in arthur.knight["potion"]["effect"]:
    #         arthur.knight["hp"] += arthur.knight["potion"]["effect"]["hp"]

    # mordred.knight
    mordred = Preparation(knightsConfig["mordred"])

    # # apply armour
    # mordred.knight["protection"] = 0
    # for a in mordred.knight["armour"]:
    #     mordred.knight["protection"] += a["protection"]
    #
    # # apply weapon
    # mordred.knight["power"] += mordred.knight["weapon"]["power"]
    #
    # # apply potion if exist
    # if mordred.knight["potion"] is not None:
    #     if "power" in mordred.knight["potion"]["effect"]:
    #         mordred.knight["power"] += mordred.knight["potion"]["effect"]["power"]
    #
    #     if "protection" in mordred.knight["potion"]["effect"]:
    #         mordred.knight["protection"] += mordred.knight["potion"]["effect"]["protection"]
    #
    #     if "hp" in mordred.knight["potion"]["effect"]:
    #         mordred.knight["hp"] += mordred.knight["potion"]["effect"]["hp"]

    # red_knight.knight
    red_knight = Preparation(knightsConfig["red_knight"])

    # # apply armour
    # red_knight.knight["protection"] = 0
    # for a in red_knight.knight["armour"]:
    #     red_knight.knight["protection"] += a["protection"]
    #
    # # apply weapon
    # red_knight.knight["power"] += red_knight.knight["weapon"]["power"]
    #
    # # apply potion if exist
    # if red_knight.knight["potion"] is not None:
    #     if "power" in red_knight.knight["potion"]["effect"]:
    #         red_knight.knight["power"] += red_knight.knight["potion"]["effect"]["power"]
    #
    #     if "protection" in red_knight.knight["potion"]["effect"]:
    #         red_knight.knight["protection"] += red_knight.knight["potion"]["effect"]["protection"]
    #
    #     if "hp" in red_knight.knight["potion"]["effect"]:
    #         red_knight.knight["hp"] += red_knight.knight["potion"]["effect"]["hp"]

    # -------------------------------------------------------------------------------
    # BATTLE:

    # 1 Lancelot vs Mordred:
    lancelot.knight["hp"] -= mordred.knight["power"] - lancelot.knight["protection"]
    mordred.knight["hp"] -= lancelot.knight["power"] - mordred.knight["protection"]

    # check if someone fell in battle_test
    if lancelot.knight["hp"] <= 0:
        lancelot.knight["hp"] = 0

    if mordred.knight["hp"] <= 0:
        mordred.knight["hp"] = 0

    # 2 Arthur vs Red Knight:
    arthur.knight["hp"] -= red_knight.knight["power"] - arthur.knight["protection"]
    red_knight.knight["hp"] -= arthur.knight["power"] - red_knight.knight["protection"]

    # check if someone fell in battle_test
    if arthur.knight["hp"] <= 0:
        arthur.knight["hp"] = 0

    if red_knight.knight["hp"] <= 0:
        red_knight.knight["hp"] = 0

    # Return battle_test results:
    return {
        lancelot.knight["name"]: lancelot.knight["hp"],
        arthur.knight["name"]: arthur.knight["hp"],
        mordred.knight["name"]: mordred.knight["hp"],
        red_knight.knight["name"]: red_knight.knight["hp"],
    }


print(battle(KNIGHTS))
