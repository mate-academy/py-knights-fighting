from app.battle.battle import Battle


def battle(base_knights: dict[dict]) -> dict:
    lancelot = None
    arthur = None
    mordred = None
    red_knight = None

    for knight_name, knight_data in base_knights.items():
        if knight_name == "lancelot":
            lancelot = Battle.knight_prepares_for_battle(knight_data)
        if knight_name == "arthur":
            arthur = Battle.knight_prepares_for_battle(knight_data)
        if knight_name == "mordred":
            mordred = Battle.knight_prepares_for_battle(knight_data)
        if knight_name == "red_knight":
            red_knight = Battle.knight_prepares_for_battle(knight_data)
    duel_1 = Battle.knights_duel(lancelot, mordred)
    duel_2 = Battle.knights_duel(arthur, red_knight)
    tournament_result = {**duel_1, **duel_2}
    print(tournament_result)
    return tournament_result
