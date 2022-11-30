from app.create_knight_instance import Knight


def battle(knights: dict):
    # CREATE CLASS INSTANCE FOR EVERY SINGLE KNIGHT

    lancelot = Knight.create_instance_from_dict(knights["lancelot"])
    arthur = Knight.create_instance_from_dict(knights["arthur"])
    mordred = Knight.create_instance_from_dict(knights["mordred"])
    red_knight = Knight.create_instance_from_dict(knights["red_knight"])

    # BATTLE PREPARATIONS:
    lancelot.apply_features()
    arthur.apply_features()
    mordred.apply_features()
    red_knight.apply_features()

    # BATTLE:

    # 1 Lancelot vs Mordred:
    lancelot.battle(mordred)
    mordred.battle(lancelot)

    # 2 Arthur vs Red Knight:
    arthur.battle(red_knight)
    red_knight.battle(arthur)

    # Return battle results:
    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }
