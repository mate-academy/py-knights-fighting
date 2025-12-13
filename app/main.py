from app.knights import Knight
from app.battle import fight


def battle(knights_config: dict[str, dict]) -> dict[str, int]:
    lancelot = Knight(knights_config["lancelot"])
    mordred = Knight(knights_config["mordred"])
    arthur = Knight(knights_config["arthur"])
    red_knight = Knight(knights_config["red_knight"])

    results = {}
    for pair in [(lancelot, mordred), (arthur, red_knight)]:
        outcome = fight(*pair)
        results.update(outcome)

    return results
