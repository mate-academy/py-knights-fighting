from app.knights.knight_dictionary import KNIGHTS
from app.battle.battle_knight import knight_initialization, knight_battle


def battle(knights_config: dict) -> dict:
    knight_dict = {}
    for knight in knights_config.values():
        knight_dict.update({knight["name"]: knight_initialization(knight)})

    knight_battle(knight_1=knight_dict["Lancelot"],
                  knight_2=knight_dict["Mordred"])
    knight_battle(knight_1=knight_dict["Arthur"],
                  knight_2=knight_dict["Red Knight"])

    return {
        "Lancelot": knight_dict["Lancelot"].hp,
        "Arthur": knight_dict["Arthur"].hp,
        "Mordred": knight_dict["Mordred"].hp,
        "Red Knight": knight_dict["Red Knight"].hp,
    }


print(battle(KNIGHTS))
