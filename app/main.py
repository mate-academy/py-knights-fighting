from app.knights.knights_preparing import prepare_knights
from app.knights.create_knight import current_knights_hps, create_knight
from app.battle.fight import fight


def battle(knights_config: dict) -> dict:

    """summing up combat characteristics for each knight"""
    # creating dict where:
    # keys - knights names
    # values - total knights characteristics:
    knights = prepare_knights(knights_config)

    # create each knight:
    lancelot = create_knight("Lancelot", knights)
    arthur = create_knight("Arthur", knights)
    mordred = create_knight("Mordred", knights)
    red_knight = create_knight("Red Knight", knights)
    # 1 Lancelot vs Mordred:
    fight(lancelot, mordred)

    # 2 Arthur vs Red Knight:
    fight(arthur, red_knight)

    # current hp of each knight after battle
    return current_knights_hps()
