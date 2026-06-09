from app.knights.knight import Knight


def battle_preparations(knights: list) -> None:
    for knight in knights:
        knight.apply_armour()
        knight.apply_weapon()
        knight.apply_potion()


def battle(knights_config: dict) -> dict:
    lancelot = Knight(knights_config["lancelot"])
    arthur = Knight(knights_config["arthur"])
    mordred = Knight(knights_config["mordred"])
    red_knight = Knight(knights_config["red_knight"])

    battle_preparations([lancelot, arthur, mordred, red_knight])

    Knight.battle_between_two(lancelot, mordred)
    Knight.battle_between_two(arthur, red_knight)

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp
    }
