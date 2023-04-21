from app.battle.all_knights import KNIGHTS
from app.battle.knight_creator import Knight
from app.battle.battle_creator import members_list
from app.battle.battle_creator import pvp_list
from app.battle.battle_creator import pvp_battle
from app.battle.battle_creator import members_sort


def battle(knights_config: dict) -> object:

    # Create a list of Knight objects from the configuration dictionary
    members = members_list(knights_config, Knight)

    # Generate all possible pairs of Knights
    members_pairs = pvp_list(members)

    # Simulate battles between each pair of Knights
    result = [
        knight
        for battle_result in [pvp_battle(pair) for pair in members_pairs]
        for knight in battle_result
    ]

    # Sort the list of winners in order of decreasing health
    result.sort(key=members_sort)

    # Create a dictionary with the names keys and health values
    return {knight.name: knight.hp for knight in result}


# Print the battle simulation using the KNIGHTS dictionary
print(dict(battle(KNIGHTS)))
