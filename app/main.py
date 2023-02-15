from app.battle.battle import Battle
from app.battle.knight import Knight
from app.configs import knights


def battle(knights_config: dict[dict]) -> dict:
    championship = Battle()

    championship.initialize_items(knights_config)
    championship.initialize_knights(knights_config)
    championship.apply_item_effects(Knight.knight_dict)

    # knight_dict is a dict of instances of Knight
    knight_dict = Knight.knight_dict

    match_1 = Battle.match(knight_dict["Lancelot"], knight_dict["Mordred"])
    match_2 = Battle.match(knight_dict["Artur"], knight_dict["Red Knight"])

    return {
        "Lancelot": match_1["Lancelot"],
        "Mordred": match_1["Mordred"],
        "Artur": match_2["Artur"],
        "Red Knight": match_2["Red Knight"],
    }


print(battle(knights))
