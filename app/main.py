import copy
import random

from app.heroes.battle import KNIGHTS


def prepare_knight(knight: dict) -> None:
    """Preparing"""
    knight["protection"] = sum(
        armor["protection"] for armor in knight["armour"]
    )
    knight["power"] += knight["weapon"]["power"]

    bonus = [
        {"name": "Orc Sword", "effect": {"hp": 10, "power": 15, "protection": -5}},
        {"name": "Druid Drinks", "effect": {"hp": 40, "power": 0, "protection": 5}},
        {"name": "Blood Blade", "effect": {"hp": 0, "power": 20, "protection": 3}},
        {"name": "Paladin Helm", "effect": {"hp": 30, "power": -5, "protection": 20}},
    ]


    effect = random.choice(bonus)["effect"]

    knight["power"] += effect.get("power", 0)
    knight["protection"] += effect.get("protection", 0)
    knight["hp"] += effect.get("hp", 0)


def duel(knight1: dict, knight2: dict) -> None:
    """Duel"""
    knight1["hp"] -= max(0, knight2["power"] - knight1["protection"])
    knight2["hp"] -= max(0, knight1["power"] - knight2["protection"])

    knight1["hp"] = max(0, knight1["hp"])
    knight2["hp"] = max(0, knight2["hp"])


def battle(knightsconfig: dict) -> dict:
    knights = copy.deepcopy(knightsconfig)

    # Knights
    for name in ["lancelot", "arthur", "mordred", "red_knight"]:
        prepare_knight(knights[name])

    # Duel
    duel(knights["lancelot"], knights["mordred"])
    duel(knights["arthur"], knights["red_knight"])

    # Results
    return {
        knights["lancelot"]["name"]: knights["lancelot"]["hp"],
        knights["arthur"]["name"]: knights["arthur"]["hp"],
        knights["mordred"]["name"]: knights["mordred"]["hp"],
        knights["red_knight"]["name"]: knights["red_knight"]["hp"],
    }


print(battle(KNIGHTS))
print(KNIGHTS)
