from app.data_base.db import KNIGHTS
from app.knights_config.character_configuration import Character
from app.battle.battle_knights import Battle


def battle(knights_config: dict) -> dict:
    # BATTLE PREPARATIONS:
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

    # -------------------------------------------------------------------------------
    # BATTLE:

    return Battle(
        lancelot=lancelot,
        arthur=arthur,
        mordred=mordred,
        red_knight=red_knight
    ).battle_knight()


print(battle(KNIGHTS))
