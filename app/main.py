from app.battle_preparations.prepare_to_battle import preparations


def battle(knights: dict) -> dict:
    knights_instances = preparations(knights)
    lancelot, arthur, mordred, red_knight = knights_instances

    lancelots_attack = lancelot.attack(mordred.hp, mordred.protection)

    if lancelots_attack <= 0:
        mordred.hp = 0
    else:
        mordred.hp = lancelots_attack

    mordreds_attack = mordred.attack(lancelot.hp, lancelot.protection)

    if mordreds_attack <= 0:
        lancelot.hp = 0
    else:
        lancelot.hp = mordreds_attack

    arthur_attack = arthur.attack(red_knight.hp, red_knight.protection)
    if arthur_attack <= 0:
        red_knight.hp = 0
    else:
        red_knight.hp = arthur_attack

    red_knight_attack = red_knight.attack(arthur.hp, arthur.protection)
    if red_knight_attack <= 0:
        arthur.hp = 0
    else:
        arthur.hp = red_knight_attack

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp
    }
