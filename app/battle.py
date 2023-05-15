def fight(knight1: dict, knight2: dict) -> int:
    knight1["hp"] -= max(0, knight2["power"] - knight1["protection"])
    knight2["hp"] -= max(0, knight1["power"] - knight2["protection"])
    knight1["hp"] = max(0, knight1["hp"])
    knight2["hp"] = max(0, knight2["hp"])


def battle(knightsconfig: dict) -> int:
    lancelot = apply_items(knightsconfig["lancelot"])
    arthur = apply_items(knightsconfig["arthur"])
    mordred = apply_items(knightsconfig["mordred"])
    red_knight = apply_items(knightsconfig["red_knight"])

    # BATTLE :
    # 1 Lancelot vs Mordred:
    fight(lancelot, mordred)

    # 2 Arthur vs Red Knight:
    fight(arthur, red_knight)

    # Return battle results:
    return {
        lancelot["name"]: lancelot["hp"],
        arthur["name"]: arthur["hp"],
        mordred["name"]: mordred["hp"],
        red_knight["name"]: red_knight["hp"],
    }


def apply_items(knight: dict) -> int:
    knight["protection"] = 0
    for armour_list in knight["armour"]:
        knight["protection"] += armour_list["protection"]

    knight["power"] += knight["weapon"]["power"]

    # apply potion if exists
    if knight["potion"] is not None:
        for main_stats in knight["potion"]["effect"]:
            if main_stats in knight:
                knight[main_stats] += knight["potion"]["effect"][main_stats]

    return knight
