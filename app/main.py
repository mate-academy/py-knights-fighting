from app.entities.knight import Knight
from app.battle.battle import Battle


def battle(knights_config: dict) -> dict:
    results = {}

    order = ["arthur", "lancelot", "mordred", "red_knight"]

    for opponent_key in order[1:]:
        # каждый бой — с НОВЫМИ объектами
        arthur = Knight("Arthur", knights_config["arthur"])
        opponent_cfg = knights_config[opponent_key]
        opponent = Knight(opponent_cfg["name"], opponent_cfg)

        fight = Battle(arthur, opponent)
        fight.start()

        results[arthur.name] = max(arthur.hp, 0)
        results[opponent.name] = max(opponent.hp, 0)

    return results
