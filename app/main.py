from app.knights import knights
from app.battle import Battle


def battle(knights_config: dict) -> dict:

    big_great_battle = Battle()
    big_great_battle.call_the_knight(knights_config)
    # BATTLE PREPARATIONS:
    big_great_battle.prepare()
    # BATTLE:
    big_great_battle.battle([
        "Lancelot vs Mordred",
        "Arthur vs Red Knight",
    ])
    return big_great_battle.print_results()


battle(knights)
