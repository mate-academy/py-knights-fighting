from app.knights.knight_dictionary import KNIGHTS
from app.battle.battle_knight import knight_initialization, knight_battle


def battle(knights_config: dict) -> dict:
    knight_dict = {
        name: knight_initialization(data)
        for name, data in knights_config.items()
    }
    knight_battle(knight_1=knight_dict["lancelot"],
                  knight_2=knight_dict["mordred"])
    knight_battle(knight_1=knight_dict["arthur"],
                  knight_2=knight_dict["red_knight"])

    return {
        "Lancelot": knight_dict["lancelot"].hp,
        "Arthur": knight_dict["arthur"].hp,
        "Mordred": knight_dict["mordred"].hp,
        "Red Knight": knight_dict["red_knight"].hp,
    }


print(battle(KNIGHTS))
