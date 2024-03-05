from app.knight.person import Knight


def battle(knights: dict[dict]) -> dict:
    participants = [Knight(knights[person]) for person in knights]
    # start preparation
    for participant in participants:
        participant.apply_armour()
        participant.equip_weapon()
        participant.use_potion()
    # battle
    for i in range(2):
        participants[i].hp -= participants[i + 2].power - participants[i].protection
        participants[i + 2].hp -= participants[i].power - participants[i + 2].protection
    for participant in participants:
        if participant.hp <= 0:
            participant.hp = 0
    return {knight.name: knight.hp for knight in participants}
