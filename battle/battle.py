from battle.knight import Knight


def battle(knights: dict) -> dict:
    lancelot = Knight.from_dict(knights["lancelot"])
    mordred = Knight.from_dict(knights["mordred"])
    arthur = Knight.from_dict(knights["arthur"])
    red_knight = Knight.from_dict(knights["red_knight"])

    lancelot.perform_battle(mordred)
    arthur.perform_battle(red_knight)

    return {
        lancelot.name: lancelot.hp,
        mordred.name: mordred.hp,
        arthur.name: arthur.hp,
        red_knight.name: red_knight.hp
    }
