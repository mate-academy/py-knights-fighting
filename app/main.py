try:
    from knights import Knight
except ImportError:
    from app.knights import Knight


def battle(knights_config: dict) -> dict[str, int]:
    # BATTLE PREPARATIONS:

    knight_list = [Knight(knight) for knight in knights_config.values()]

    # -------------------------------------------------------------------------------
    # BATTLE:

    for i in range(len(knight_list) // 2):
        knight_list[i].fight(knight_list[i + 2])

    # Return battle results:
    return {knight.name: knight.hp for knight in knight_list}
