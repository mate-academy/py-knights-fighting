from app.knight.person import Knight


def battle(knights: dict[dict]) -> dict:
    heroes = [Knight(knights[person]) for person in knights]
    # start preparation
    for participant in heroes:
        participant.apply_armour()
        participant.equip_weapon()
        participant.use_potion()
    # battle
    for i in range(2):
        heroes[i].hp -= heroes[i + 2].power - heroes[i].protection
        heroes[i + 2].hp -= heroes[i].power - heroes[i + 2].protection
    for participant in heroes:
        if participant.hp <= 0:
            participant.hp = 0
    return {knight.name: knight.hp for knight in heroes}
