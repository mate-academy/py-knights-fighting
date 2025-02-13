from app.init_data import Knight


def init_knights(knights_config: dict) -> dict:
    knights = {}
    for name, knight in knights_config.items():
        knights[name] = Knight(**knight)
    return knights


def attack(knight: Knight, other_knight: Knight) -> dict:
    damage_to_other = max(0, knight.power - other_knight.protection)
    damage_to_self = max(0, other_knight.power - knight.protection)

    other_knight.hp = max(0, other_knight.hp - damage_to_other)
    knight.hp = max(0, knight.hp - damage_to_self)

    fight_result = {
        knight.name: knight.hp,
        other_knight.name: other_knight.hp,
    }

    return fight_result
