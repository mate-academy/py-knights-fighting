from typing import Dict, Any


def battle_round(fighter1: Dict[str, Any], fighter2: Dict[str, Any]) -> None:

    fighter1["hp"] -= max(0, fighter2["power"] - fighter1["protection"])
    fighter2["hp"] -= max(0, fighter1["power"] - fighter2["protection"])

    # check if someone fell in battle
    fighter1["hp"] = max(fighter1["hp"], 0)
    fighter2["hp"] = max(fighter2["hp"], 0)
