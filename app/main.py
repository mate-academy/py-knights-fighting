from app.Knights.preparation import Knight
from app.Knights.battle import Battle


def battle(knights_config: dict) -> dict:
    for knight, info in knights_config.items():
        knight = Knight(name=info["name"],
                        power=info["power"],
                        hp=info["hp"])
        Knight.knights_dict[info["name"]] = knight
        knight_update = Knight.knights_dict[info["name"]]
        knight_update.update(armour=info["armour"],
                             weapon=info["weapon"],
                             potion=info["potion"])

    # BATTLE STAGE

    Battle.fight(first=Knight.knights_dict["Lancelot"],
                 second=Knight.knights_dict["Mordred"])
    Battle.fight(first=Knight.knights_dict["Artur"],
                 second=Knight.knights_dict["Red Knight"])
    return Battle.battle_result(Knight.knights_dict)
