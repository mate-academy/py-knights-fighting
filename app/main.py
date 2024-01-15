from app.battle.contest import Contest
from app.data.data import KNIGHTS


def battle(knights_config: dict) -> dict:
    # BATTLE PREPARATIONS:
    championship2024 = Contest()
    championship2024.create_knight_instances(knights_config)
    championship2024.prepare_for_battle()

    # -------------------------------------------------------------------------------
    # BATTLE:
    championship2024.start_battles()
    result = championship2024.get_contest_results()

    return result


print(battle(KNIGHTS))
