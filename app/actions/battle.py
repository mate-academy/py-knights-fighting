from app.actions.register import register_knights


def battle(registered_knights: list) -> dict:
    if isinstance(registered_knights, dict):
        registered_knights = register_knights(registered_knights)

    for knight in registered_knights:
        knight.prepare_for_battle()

    registered_knights[0].hp -= (registered_knights[2].power
                                 - registered_knights[0].protection)
    registered_knights[2].hp -= (registered_knights[0].power
                                 - registered_knights[2].protection)

    registered_knights[1].hp -= (registered_knights[3].power
                                 - registered_knights[1].protection)
    registered_knights[3].hp -= (registered_knights[1].power
                                 - registered_knights[3].protection)

    for knight in registered_knights:
        if knight.hp <= 0:
            knight.hp = 0

    results = {}

    for knight in registered_knights:
        results[knight.name] = knight.hp

    return results
