from app.championship.championship_class import Championship
from app.knight.knights_data import KNIGHTS
from app.knight.knight_class import Knight


def battle(knights_config: dict) -> dict:
    """
    Carry out Knight's championship battles, display their results.
    :param knights_config:
    :return: a dictionary of Knight instances
    """
    championship = Championship()
    knights = Knight.get_knights(knights_config)
    championship.fight(knights["Lancelot"], knights["Mordred"])
    championship.fight(knights["Arthur"], knights["Red Knight"])
    return championship.get_championship_results()


print(battle(KNIGHTS))
