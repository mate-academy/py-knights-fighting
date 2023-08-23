from app.knights.dict_to_knight import hero_initialise, knights_info


def battle(knights_inform: dict) -> dict:
    heroes_list = hero_initialise(knights_inform)
    lancelot, arthur, mordred, red_knight = heroes_list
    for knight in heroes_list:
        knight.calculate_stats()

    lancelot.versus_step(mordred)
    arthur.versus_step(red_knight)

    return {
        lancelot.name: lancelot.health_point,
        arthur.name: arthur.health_point,
        mordred.name: mordred.health_point,
        red_knight.name: red_knight.health_point,
    }


battle(knights_info)
