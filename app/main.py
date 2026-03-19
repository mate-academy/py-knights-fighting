from app.battles.fight import fight
from app.conquerors.conquerors import calculate_stats


def battle(stats: dict) -> dict:
    battles = [("lancelot", "mordred"), ("arthur", "red_knight")]

    return {
        k: v
        for knight1, knight2 in battles
        for k, v in fight(calculate_stats(stats[knight1]),
                          calculate_stats(stats[knight2])).items()
    }
