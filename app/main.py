from app.knights.knight import Knight
from app.logic.fight import get_fight
from app.logic.check_hp import check_hp


def battle(knights_config: dict) -> dict:
    # BATTLE PREPARATIONS:
    knights = {}

    for knight_id, config in knights_config.items():
        knight = Knight(config)
        knight.apply_potion()
        knights[knight_id] = knight

    # -------------------------------------------------------------------------------
    # BATTLE:

    # 1 Lancelot vs Mordred:
    get_fight(knights["lancelot"], knights["mordred"])
    # 2 Arthur vs Red Knight:
    get_fight(knights["arthur"], knights["red_knight"])

    # check if someone fell in battle
    for knight in knights.values():
        check_hp(knight)

    # Return battle results:
    return {
        knight.name: knight.hp
        for knight in knights.values()
    }
