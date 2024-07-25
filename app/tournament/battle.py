def apply_skills(participants: dict, participating_knights: dict) -> None:
    for nickname in participating_knights:
        knight = participating_knights[nickname]
        if participants[nickname]["armour"]:
            knight.apply_armour(participants[nickname]["armour"])
        knight.apply_weapon(participants[nickname]["weapon"])
        if participants[nickname]["potion"]:
            knight.apply_potion(participants[nickname]["potion"]["effect"])


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
