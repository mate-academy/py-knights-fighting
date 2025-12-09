from app.Knights.models import Knight


def create_knights(knights_config: dict) -> dict[str, Knight]:
    knights = {}
    for key, config in knights_config.items():
        knights[key] = Knight.from_config(config)
    return knights


def duel(first_knight: Knight, second_knight: Knight) -> None:
    damage_to_first = max(0, second_knight.power - first_knight.protection)
    damage_to_second = max(0, first_knight.power - second_knight.protection)

    first_knight.hp -= damage_to_first
    second_knight.hp -= damage_to_second

    if first_knight.hp < 0:
        first_knight.hp = 0
    if second_knight.hp < 0:
        second_knight.hp = 0


def battle(knights_config: dict) -> dict[str, int]:
    knights = create_knights(knights_config)

    lancelot = knights["lancelot"]
    mordred = knights["mordred"]
    arthur = knights["arthur"]
    red_knight = knights["red_knight"]

    duel(lancelot, mordred)
    duel(arthur, red_knight)

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }
