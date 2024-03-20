from tests.default_config import fights_config
from app.knights.characters import Knight
from app.knights.fight import Fight


def battle(knights_config: dict) -> dict:
    knights = {}

    for name, properties in knights_config.items():
        knight = Knight(**properties)
        knights.update({name: knight})

    # Lancelot vs Mordred:
    Fight(knights["lancelot"], knights["mordred"]).fight_hit()
    # Arthur vs Red Knight:
    Fight(knights["arthur"], knights["red_knight"]).fight_hit()

    return {knight.name: knight.hp for knight in knights.values()}


if __name__ == "__main__":
    print(battle(fights_config))
