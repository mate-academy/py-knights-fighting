from app.utils.prepare import prepare_knight
from app.utils.fight import fight


def battle(knights_config: dict) -> dict:
    lancelot = prepare_knight(knights_config["lancelot"])
    mordred = prepare_knight(knights_config["mordred"])
    arthur = prepare_knight(knights_config["arthur"])
    red_knight = prepare_knight(knights_config["red_knight"])

    result = {}
    result.update(fight(lancelot, mordred))
    result.update(fight(arthur, red_knight))

    return result

