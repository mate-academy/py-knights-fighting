def make_tournament(participants: dict) -> dict:
    result_battle = {}
    for nick in participants:
        knight1 = participants[nick]
        if knight1.name not in result_battle:
            knight1.fighting()
        knight2 = knight1.opponent
        result_battle[knight1.name] = knight1.hp
        result_battle[knight2.name] = knight2.hp
    return result_battle
