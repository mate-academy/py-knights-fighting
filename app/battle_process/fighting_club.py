import random
from typing import Any


def fight_knights(knight_config: dict) -> Any:
    knights_list = list(knight_config.values())
    # Pair up the knights for duels
    random.shuffle(knights_list)
    pairs = [
        (knights_list[i], knights_list[i + 1])
        for i in range(0, len(knights_list), 2)
    ]

    # Perform duels
    for knight1, knight2 in pairs:
        # Calculate damage for each knight
        damage_knight1 = knight2["power"] - knight1["protection"]
        damage_knight2 = knight1["power"] - knight2["protection"]

        # Update HP for each knight
        knight1["hp"] -= damage_knight1
        knight2["hp"] -= damage_knight2

        # Check if any knight's HP falls below 0
        if knight1["hp"] < 0:
            knight1["hp"] = 0
        if knight2["hp"] < 0:
            knight2["hp"] = 0
    # Determine the winner
        if pairs:
            if knight1["hp"] > knight2["hp"]:
                return (f'Knight {knight1["name"]} is the winner!'
                        f' Winner hp: {knight1["hp"]}')
            elif knight2["hp"] > knight1["hp"]:
                return (f'Knight {knight2["name"]} is the winner!'
                        f' Winner hp: {knight2["hp"]}')
            else:
                return "It's a draw!"
        else:
            return "No knights available for dueling."
