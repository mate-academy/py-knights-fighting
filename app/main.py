from app.data_base.data_base_knights import KNIGHTS
from app.knights_config.character_configuration import Character
from app.battle.battle_knights import Battle


def battle(knights_config: dict) -> dict:
    lancelot = Character(name_knight="lancelot", knight=knights_config)
    arthur = Character(name_knight="arthur", knight=knights_config)
    mordred = Character(name_knight="mordred", knight=knights_config)
    red_knight = Character(name_knight="red_knight", knight=knights_config)

    Battle(lancelot, mordred).battle_knight()
    Battle(arthur, red_knight).battle_knight()

    return Battle.result


print(battle(KNIGHTS))
