from app.data_base.data_base_knights import KNIGHTS
from app.knights_config.character_configuration import Character
from app.battle.battle_knights import Battle


def battle(knights_config: dict) -> dict:
    lancelot = Character(
        name_knight="lancelot",
        knight=knights_config
    ).new_character()

    arthur = Character(
        name_knight="arthur",
        knight=knights_config
    ).new_character()

    mordred = Character(
        name_knight="mordred",
        knight=knights_config
    ).new_character()

    red_knight = Character(
        name_knight="red_knight",
        knight=knights_config
    ).new_character()

    Battle(one_knight=lancelot, two_knight=mordred).battle_knight()
    Battle(one_knight=arthur, two_knight=red_knight).battle_knight()

    return Battle.result


print(battle(KNIGHTS))
