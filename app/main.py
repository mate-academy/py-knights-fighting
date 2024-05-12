from app.characteristics_of_a_knight.knight import change_in_characteristics
from app.Battle.battle_knight import fight_of_knights
from app.knights_config import KNIGHTS


def battle(knights_config: dict) -> dict:

    lancelot = change_in_characteristics(
        knights_configs=knights_config["lancelot"])

    arthur = change_in_characteristics(
        knights_configs=knights_config["arthur"])

    mordred = change_in_characteristics(
        knights_configs=knights_config["mordred"])

    red_knight = change_in_characteristics(
        knights_configs=knights_config["red_knight"])

    fight_of_knights(lancelot, mordred)
    fight_of_knights(arthur, red_knight)
    return {
        lancelot["name"]: lancelot["hp"],
        arthur["name"]: arthur["hp"],
        mordred["name"]: mordred["hp"],
        red_knight["name"]: red_knight["hp"],
    }


print(battle(KNIGHTS))
