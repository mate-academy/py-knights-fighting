from app.Knights.preparation import Knight
from app.Knights.battle import Battle


def battle(knights_config: dict) -> dict:
    Knight.upgrade(knights_config=knights_config)

    # BATTLE STAGE

    Battle.fight(first=Knight.knights_dict["Lancelot"],
                 second=Knight.knights_dict["Mordred"])
    Battle.fight(first=Knight.knights_dict["Artur"],
                 second=Knight.knights_dict["Red Knight"])
    return Battle.battle_result(Knight.knights_dict)
