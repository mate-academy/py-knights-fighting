from app.entities.knight import Knight


def battle(knights_config: dict) -> dict:
    knights = {}

    for key, config in knights_config.items():
        knights[key] = Knight(config["name"], config)

    # дальше будет логика боёв (следующий шаг)

    return {
        knight.name: max(knight.hp, 0)
        for knight in knights.values()
    }


if __name__ == "__main__":
    pass
