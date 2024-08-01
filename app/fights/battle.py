def battle(knights: dict) -> dict:
    lancelot = knights["lancelot"]
    mordred = knights["mordred"]
    arthur = knights["arthur"]
    red_knight = knights["red_knight"]

    lancelot.hp -= max(mordred.power - lancelot.protection, 0)
    mordred.hp -= max(lancelot.power - mordred.protection, 0)

    arthur.hp -= max(red_knight.power - arthur.protection, 0)
    red_knight.hp -= max(arthur.power - red_knight.protection, 0)

    results = {
        lancelot.name: max(lancelot.hp, 0),
        mordred.name: max(mordred.hp, 0),
        arthur.name: max(arthur.hp, 0),
        red_knight.name: max(red_knight.hp, 0),
    }
    return results
