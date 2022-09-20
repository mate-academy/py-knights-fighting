from app.knights import Knight


def battle(knights) -> dict:
    lancelot = Knight(knights["lancelot"])
    lancelot.prepare_to_battle()

    arthur = Knight(knights["arthur"])
    arthur.prepare_to_battle()

    mordred = Knight(knights["mordred"])
    mordred.prepare_to_battle()

    red_knight = Knight(knights["red_knight"])
    red_knight.prepare_to_battle()

    lancelot.attack_enemy(mordred)
    mordred.attack_enemy(lancelot)

    lancelot.hp_check()
    mordred.hp_check()

    arthur.attack_enemy(red_knight)
    red_knight.attack_enemy(arthur)

    arthur.hp_check()
    red_knight.hp_check()

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }
