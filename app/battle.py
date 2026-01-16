from app.knight import Knight


def battle_from_config(knights_config: dict) -> dict:
    knights = {name: Knight(**data) for name, data in knights_config.items()}
    return battle_from_objects(knights)


def battle_from_objects(knights: dict[str, Knight]) -> dict:
    for knight in knights.values():
        knight.prepare()

    knights["lancelot"].battle_knights(knights["mordred"])
    knights["arthur"].battle_knights(knights["red_knight"])

    return {
        knight.name: knight.hp for knight in knights.values()
    }
