from app.knight import Knight


def battle_vs(knight_1: Knight, knight_2: Knight) -> None:
    # Battle of knights
    knight_1.hp -= knight_2.power - knight_1.protection
    knight_2.hp -= knight_1.power - knight_2.protection

    # Check if someone fell in battle
    knight_1.check_hp()
    knight_2.check_hp()


def battle(knights_config: dict) -> dict:
    lancelot = Knight(knights_config["lancelot"])
    mordred = Knight(knights_config["mordred"])
    arthur = Knight(knights_config["arthur"])
    red_knight = Knight(knights_config["red_knight"])

    # Battle preparations
    lancelot.battle_preparations()
    mordred.battle_preparations()
    arthur.battle_preparations()
    red_knight.battle_preparations()

    # Battle
    battle_vs(lancelot, mordred)
    battle_vs(red_knight, arthur)

    # Return battle results:
    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }
