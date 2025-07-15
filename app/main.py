from app.battle.battle import Battle
from app.knights.knight import Knight


def battle(knights_config: dict[str, dict]) -> dict[str, int]:
    knights: dict[str, Knight] = {}

    for config in knights_config:
        knight = Knight(knights_config[config])

        knight.prepare_to_battle()

        knights[knight.name] = knight

    Battle.perform_battle(knights["Lancelot"], knights["Mordred"])
    Battle.perform_battle(knights["Arthur"], knights["Red Knight"])

    return {
        name: knights.get(name).hp
        for name in knights
    }
