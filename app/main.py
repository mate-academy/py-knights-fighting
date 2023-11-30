from app.battle_preparations.prepare_to_battle import prepare_to_battle


def battle(knights: dict) -> dict:
    knights_instances = prepare_to_battle(knights)
    lancelot, arthur, mordred, red_knight = knights_instances

    lancelot.defend(mordred.power)
    mordred.defend(lancelot.power)
    arthur.defend(red_knight.power)
    red_knight.defend(arthur.power)

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp
    }
