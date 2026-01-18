from app.entities.knight import Knight
from app.battle.battle import Battle


def battle(knights_config: dict) -> dict:
    knights = {
        key: Knight(config["name"], config)
        for key, config in knights_config.items()
    }

    order = ["arthur", "lancelot", "mordred", "red_knight"]

    current_knight = knights[order[0]]

    for next_key in order[1:]:
        enemy = knights[next_key]

        fight = Battle(current_knight, enemy)
        result = fight.start()

        # определяем победителя
        if result[current_knight.name] > 0:
            current_knight = current_knight
        else:
            current_knight = enemy

    return {
        knight.name: max(knight.hp, 0)
        for knight in knights.values()
    }
