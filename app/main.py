from app.KnightsManager import KnightsManager


def battle(knights_config: dict) -> dict:

    knights_manager = KnightsManager()

    knights_manager.load_knights_config(knights_config)

    lancelot = knights_manager.get_knight_by_name("lancelot")
    arthur = knights_manager.get_knight_by_name("arthur")
    mordred = knights_manager.get_knight_by_name("mordred")
    red_knight = knights_manager.get_knight_by_name("red_knight")

    for knight in knights_manager.all_knights.values():
        knight.prepare_for_fight()

    knights_manager.fight_between(lancelot, mordred)
    knights_manager.fight_between(arthur, red_knight)

    return knights_manager.knights_summary()
