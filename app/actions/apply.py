from __future__ import annotations


def apply_armour(player: "knightsConfig") -> None:
    player["protection"] = 0
    for a in player["armour"]:
        player["protection"] += a["protection"]


def apply_weapon(player: "knightsConfig") -> None:
    player["power"] += player["weapon"]["power"]


def apply_potion_if_exist(player: "knightsConfig") -> None:
    if player["potion"]:
        if "power" in player["potion"]["effect"]:
            player["power"] += player["potion"]["effect"]["power"]

        if "protection" in player["potion"]["effect"]:
            player["protection"] += player["potion"]["effect"]["protection"]

        if "hp" in player["potion"]["effect"]:
            player["hp"] += player["potion"]["effect"]["hp"]


def apply_all_for(player: "knightsConfig") -> None:
    apply_armour(player)
    apply_weapon(player)
    apply_potion_if_exist(player)
