from app.stats.knight_stat import knights_stat
from app.battle_actions import assessment


def battle(knights_config: dict) -> dict:
    return assessment.assessment(knights_config)


print(battle(knights_stat))
