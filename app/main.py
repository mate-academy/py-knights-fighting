from app.knight_parts.knight import Knight


def battle(knights: dict) -> dict:
    # BATTLE PREPARATIONS:

    knight_instances = {
        key: Knight.convert_to_knight(knight)
        for key, knight in knights.items()
    }
    for knight in knight_instances.values():
        knight.prepare_for_battle()

    lancelot = knight_instances.get("lancelot")
    arthur = knight_instances.get("arthur")
    mordred = knight_instances.get("mordred")
    red_knight = knight_instances.get("red_knight")

    # -------------------------------------------------------------------------------
    # BATTLE:

    # 1 Lancelot vs Mordred:
    lancelot.fight(mordred)

    # 2 Arthur vs Red Knight:
    arthur.fight(red_knight)

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }
