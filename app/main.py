from app.data.classes import Knight


def battle(knights_config: dict) -> dict:
    lancelot = Knight(knights_config["lancelot"])
    mordred = Knight(knights_config["mordred"])
    arthur = Knight(knights_config["arthur"])
    red_knight = Knight(knights_config["red_knight"])

    def process_battle(fighter1: Knight, fighter2: Knight) -> None:
        fighter1.take_damage(fighter2.power)
        fighter2.take_damage(fighter1.power)

    process_battle(lancelot, mordred)
    process_battle(arthur, red_knight)

    return {
        lancelot.name: lancelot.hp,
        mordred.name: mordred.hp,
        arthur.name: arthur.hp,
        red_knight.name: red_knight.hp,
    }
