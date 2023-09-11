from app.championship_setup.championship_class import Championship
from app.knights_setup.knights_data import KNIGHTS


def battle(knights_config: dict) -> dict:
    """
    Carry out Knight's championship battles, display their results.
    :param knights_config:
    :return: a dictionary of Knight instances
    """
    championship = Championship(knights_config)
    knights = championship.battle_preparation()
    championship.single_battle(knights["lancelot"], knights["mordred"])
    championship.single_battle(knights["arthur"], knights["red_knight"])
    return championship.championship_results()


print(battle(KNIGHTS))
