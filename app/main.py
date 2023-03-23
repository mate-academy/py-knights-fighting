from app.knight import Knight


def battle(knights_config: dict) -> dict:
    # BATTLE PREPARATIONS:
    tournament_members = [Knight(knight) for knight in knights_config.values()]
    # -------------------------------------------------------------------------------
    # BATTLE:
    for i in range(len(tournament_members) // 2):
        Knight.battle(tournament_members[i], tournament_members[i + 2])
    # Check for the correctness of the HP
    for knight in tournament_members:
        Knight.check_correctness_hp(knight)
    # Return battle results:
    return {
        knight.name: knight.hp for knight in tournament_members
    }
