from app.Knights.KNIGHTS import KNIGHTS
from app.Knights.Preparation import PrepareKnight
from app.Knights.BATTLE import Battle


def battle(knights_config: dict) -> dict:
    for knight, info in knights_config.items():
        knight = PrepareKnight(name=info["name"],
                               power=info["power"],
                               hp=info["hp"])
        PrepareKnight.knights_dict[info["name"]] = knight
        knight_update = PrepareKnight.knights_dict[info["name"]]
        knight_update.update(armour=info["armour"],
                             weapon=info["weapon"],
                             potion=info["potion"])

    # BATTLE STAGE

    Battle.fight(first=PrepareKnight.knights_dict["Lancelot"],
                 second=PrepareKnight.knights_dict["Mordred"])
    Battle.fight(first=PrepareKnight.knights_dict["Artur"],
                 second=PrepareKnight.knights_dict["Red Knight"])
    return Battle.battle_result(PrepareKnight.knights_dict)
