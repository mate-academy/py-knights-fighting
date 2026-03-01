from app.Castle.knights import KNIGHTS, generator_of_knights


def battle(base_knights_config):
    knights = generator_of_knights(base_knights_config)

    lancelot = next(knights)
    arthur = next(knights)
    mordred = next(knights)
    red_knight = next(knights)
    lancelot.battle(mordred)
    arthur.battle(red_knight)

    battle_result = {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp
    }
    return battle_result


print(battle(KNIGHTS))
