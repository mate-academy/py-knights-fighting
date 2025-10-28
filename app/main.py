from app.knight.knight import Knight
from app.battle.battle import Battle


def battle(knights_config: dict) -> dict:
    """Simulates a battle between knights.

    :param knights_config: A dictionary containing the knight configurations.
    :type knights_config: dict
    :return: A dictionary with the final health points of the knights.
    :rtype: dict
    """
    Knight.generate_knights(knights_config)
    Knight.apply_equipment()

    Battle(Knight.knights["lancelot"], Knight.knights["mordred"])
    Battle(Knight.knights["arthur"], Knight.knights["red_knight"])

    return Battle.results
