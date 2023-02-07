from app.Knights.Preparation import Prepare
from app.Knights.Battle import Battle


def battle(knights_config: dict) -> dict:
    for knight, info in knights_config.items():
        knight = Prepare(name=info["name"],
                         power=info["power"],
                         hp=info["hp"])
        Prepare.knights_dict[info["name"]] = knight
        knight_update = Prepare.knights_dict[info["name"]]
        knight_update.update(armour=info["armour"],
                             weapon=info["weapon"],
                             potion=info["potion"])

    # BATTLE STAGE

    Battle.fight(first=Prepare.knights_dict["Lancelot"],
                 second=Prepare.knights_dict["Mordred"])
    Battle.fight(first=Prepare.knights_dict["Artur"],
                 second=Prepare.knights_dict["Red Knight"])
    return Battle.battle_result(Prepare.knights_dict)
