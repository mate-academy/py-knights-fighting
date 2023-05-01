from app.knight import Knight


def battle(resulting_dict: dict) -> dict:
    results = {}
    knights = {}
    # BATTLE PREPARATIONS:
    for knight_name, knight_stats in resulting_dict.items():
        knight = Knight(**knight_stats)
        knight.apply_stats()
        knights[knight_name] = knight

    # -------------------------------------------------------------------------------
    # BATTLE:

    # 1 Lancelot vs Mordred:
    results.update(knights["lancelot"].battle(knights["mordred"]))
    # 2 Arthur vs Red Knight:
    results.update(knights["arthur"].battle(knights["red_knight"]))
    # Return battle results:
    return {
        str(knight): results.get(knight, {})
        for knight_name, knight in knights.items()
    }
