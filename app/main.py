from app.entities.knight import Knight
from app.battle.battle import Battle


def battle(knights_config: dict) -> dict:
    result = {}

    arthur_config = knights_config["arthur"]

    for name, config in knights_config.items():
        if name == "arthur":
            continue

        arthur = Knight("arthur", arthur_config)
        enemy = Knight(name, config)

        fight = Battle(arthur, enemy)
        fight.start()

        result["arthur"] = max(arthur.hp, 0)
        result[name] = max(enemy.hp, 0)

    return result
