from app.people.knight import Knight


def battle(knight_config: dict) -> dict:
    knights = {
        name: Knight(config=config)
        for name, config in knight_config.items()
    }

    return {
        **knights["lancelot"].fight_with(knights["mordred"]),
        **knights["arthur"].fight_with(knights["red_knight"]),
    }
