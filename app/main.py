from app.fight import fight
from app.preparations import battle_preparation


def battle(knights_config: dict) -> dict:
    # BATTLE PREPARATIONS:

    # lancelot
    for knight in knights_config:
        knights_config[knight] = battle_preparation(knights_config[knight])

    # 1 Lancelot vs Mordred:
    fight_1 = fight(knights_config["lancelot"], knights_config["mordred"])

    # 2 Arthur vs Red Knight:
    fight_2 = fight(knights_config["arthur"], knights_config["red_knight"])

    fight_1.update(fight_2)
    # Return battle results:
    return fight_1
