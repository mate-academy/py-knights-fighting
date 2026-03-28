from app.modules.knights import Knight


def battle(knights_dict: dict) -> dict:

    lancelot = Knight.make_knight(knights_dict["lancelot"])
    arthur = Knight.make_knight(knights_dict["arthur"])
    mordred = Knight.make_knight(knights_dict["mordred"])
    red_knight = Knight.make_knight(knights_dict["red_knight"])

    lancelot.fight(mordred)
    arthur.fight(red_knight)

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp
    }
