from app.knights_stats1 import TheKnight
from app.scores import Scores


def battle(stats: dict) -> dict:
    contenders = TheKnight.count_stats(stats)
    first_battle = Scores.battle_scores(contenders[0], contenders[2])
    second_battle = Scores.battle_scores(contenders[1], contenders[3])
    first_battle.update(second_battle)
    return first_battle
