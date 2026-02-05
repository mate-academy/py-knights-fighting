from app.knight import Knight


def battle(knights_config: dict) -> dict[str, int]:
    knights = {key: Knight(cfg) for key, cfg in knights_config.items()}

    for knight in knights.values():
        knight.prepare()

    knights["lancelot"].fight(knights["mordred"])
    knights["arthur"].fight(knights["red_knight"])

    return {knight.name: knight.hp for knight in knights.values()}
