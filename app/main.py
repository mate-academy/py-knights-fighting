from app.data_knights.knights_info import KNIGHTS
from app.battle.battle import Battle
from app.character.knight_konfiguration import Character


def battle(knights_config: dict) -> dict:
    lancelot = Character(name="lancelot", data_knight=knights_config)
    arthur = Character(name="Arthur", data_knight=knights_config)
    mordred = Character(name="mordred", data_knight=knights_config)
    red_knight = Character(name="red_knight", data_knight=knights_config)

    Battle(lancelot, mordred).battle_of_knights()
    Battle(arthur, red_knight).battle_of_knights()

    result = {
        "Lancelot": Battle.result["lancelot"],
        "Arthur": Battle.result["Arthur"],
        "Mordred": Battle.result["mordred"],
        "Red Knight": Battle.result["red_knight"]
    }
    return result


battle(KNIGHTS)
