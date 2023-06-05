from app.services.battle import Battle
from app.constants import KNIGHTS


def battle(knights_config: dict) -> dict:
    initialized_battle = Battle(knights_config)

    return initialized_battle.start()


battle(KNIGHTS)
