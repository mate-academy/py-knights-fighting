def battle_results(knights: list) -> dict:
    for knight in knights:
        knight.prepare_for_battle()

    lancelot = knights[0]
    arthur = knights[1]
    mordred = knights[2]
    red_knight = knights[3]

    lancelot.take_damage(mordred.power - lancelot.protection)
    mordred.take_damage(lancelot.power - mordred.protection)
    lancelot.hp = max(0, lancelot.hp)
    mordred.hp = max(0, mordred.hp)

    arthur.take_damage(red_knight.power - arthur.protection)
    red_knight.take_damage(arthur.power - red_knight.protection)
    arthur.hp = max(0, arthur.hp)
    red_knight.hp = max(0, red_knight.hp)

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }
