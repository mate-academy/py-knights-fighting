from app.battle.battle import Battle


def battle(base_knights: dict[dict]) -> dict:
    tournament_result = Battle.knights_tournament(base_knights)
    return tournament_result
