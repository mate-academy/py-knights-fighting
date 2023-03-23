from app.knight import Knight


def battle(knights_config: dict) -> dict:
    # BATTLE PREPARATIONS:
    tournament_members = []

    for knight in knights_config.values():
        tournament_members.append(Knight(knight))

    # -------------------------------------------------------------------------------
    # BATTLE:
    for i in range(len(tournament_members) // 2):
        Knight.battle(tournament_members[i], tournament_members[i + 2])

    # Return battle results:
    return {
        knight.name: knight.hp for knight in tournament_members
    }
