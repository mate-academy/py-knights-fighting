from app.knights_stats1 import TheKnight
from app.scores import Scores
from app.knight_dict import knights


def battle(knights: dict) -> dict:
    list_of_knights = TheKnight.stats(knights)
    knight1 = list_of_knights[0]
    knight2 = list_of_knights[1]
    print(f"The battle between {knight1['name']} and {knight2['name']} started!")
    results = Scores.battle_scores(knight1, knight2)
    knight3 = list_of_knights[2]
    knight4 = list_of_knights[3]
    print(f"The battle between {knight3['name']} and {knight4['name']} started!")
    Scores.battle_scores(knight3, knight4)
    results.update(Scores.battle_scores(knight3, knight4))
    return results
