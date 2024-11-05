from copy import deepcopy
from app.prepare import prepare_to_fight


def to_battle(knight1: dict, knight2: dict) -> None:
    """Process a battle between two knights."""
    # Calculate damage
    knight1["hp"] -= max(0, knight2["power"] - knight1["protection"])
    knight2["hp"] -= max(0, knight1["power"] - knight2["protection"])

    # Ensure HP doesn't go below 0
    knight1["hp"] = max(0, knight1["hp"])
    knight2["hp"] = max(0, knight2["hp"])


def battle(knightsconfig: dict) -> dict:
    knights = {
        name: deepcopy(knight)
        for name, knight in knightsconfig.items()
    }

    for knight_name, knight in knights.items():
        print(knight)
        prepare_to_fight(knight)

    # Process battles
    to_battle(knights["lancelot"], knights["mordred"])
    to_battle(knights["arthur"], knights["red_knight"])

    # Return battle results:
    return {
        knight["name"]: knight["hp"]
        for knight in knights.values()
    }
