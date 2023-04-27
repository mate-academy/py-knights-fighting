def battle(knightsconfig: dict) -> int:
    def apply_items(knight: dict) -> int:
        knight["protection"] = 0
        for armour_list in knight["armour"]:
            knight["protection"] += armour_list["protection"]

        knight["power"] += knight["weapon"]["power"]

        # apply potion if exists
        if knight["potion"] is not None:
            if "power" in knight["potion"]["effect"]:
                knight["power"] += knight["potion"]["effect"]["power"]

            if "protection" in knight["potion"]["effect"]:
                knight["protection"] += \
                    knight["potion"]["effect"]["protection"]

            if "hp" in knight["potion"]["effect"]:
                knight["hp"] += knight["potion"]["effect"]["hp"]

        return knight

    lancelot = knightsconfig["lancelot"]
    arthur = knightsconfig["arthur"]

    lancelot = apply_items(lancelot)
    arthur = apply_items(arthur)

    mordred = knightsconfig["mordred"]
    red_knight = knightsconfig["red_knight"]

    mordred = apply_items(mordred)
    red_knight = apply_items(red_knight)

    # -------------------------------------------------------------------------------
    # BATTLE:
    # 1 Lancelot vs Mordred:
    lancelot["hp"] -= mordred["power"] - lancelot["protection"]
    mordred["hp"] -= lancelot["power"] - mordred["protection"]

    # check if someone fell in battle
    if lancelot["hp"] <= 0:
        lancelot["hp"] = 0

    if mordred["hp"] <= 0:
        mordred["hp"] = 0

    # 2 Arthur vs Red Knight:
    arthur["hp"] -= red_knight["power"] - arthur["protection"]
    red_knight["hp"] -= arthur["power"] - red_knight["protection"]

    # check if someone fell in battle
    if arthur["hp"] <= 0:
        arthur["hp"] = 0

    if red_knight["hp"] <= 0:
        red_knight["hp"] = 0
#
    # Return battle results:
    return {
        lancelot["name"]: lancelot["hp"],
        arthur["name"]: arthur["hp"],
        mordred["name"]: mordred["hp"],
        red_knight["name"]: red_knight["hp"],
    }
