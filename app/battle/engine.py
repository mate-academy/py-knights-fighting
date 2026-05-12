from app.battle.factory import create_knight
from app.knights.knight import Knight


def fight(knight1: Knight, knight2: Knight) -> None:
    knight1.take_damage(knight2.power)
    knight2.take_damage(knight1.power)


def battle(knights_config: dict) -> dict:
    lancelot = create_knight(
        knights_config["lancelot"]
    )

    arthur = create_knight(
        knights_config["arthur"]
    )

    mordred = create_knight(
        knights_config["mordred"]
    )

    red_knight = create_knight(
        knights_config["red_knight"]
    )

    fight(lancelot, mordred)
    fight(arthur, red_knight)

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }
