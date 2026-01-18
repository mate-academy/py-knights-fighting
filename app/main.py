from app.entities.knight import Knight
from app.battle.battle import Battle


def battle(knights_config: dict) -> dict:
    knights = {
        key: Knight(config["name"], config)
        for key, config in knights_config.items()
    }

    order = ["arthur", "lancelot", "mordred", "red_knight"]

    current = knights[order[0]]

    for next_key in order[1:]:
        enemy = knights[next_key]

        fight = Battle(current, enemy)
        fight.start()

        # победитель идёт дальше
        if current.is_alive():
            current = current
        else:
            current = enemy

    return {
        knight.name: max(knight.hp, 0)
        for knight in knights.values()
    }
