from app.services.battle import fight
from app.services.preparation import prepare_knight


def battle(knights_config: dict) -> dict:
    prepared_knights = {}

    for knight_name, knight_data in knights_config.items():
        prepared_knights[knight_name] = prepare_knight(knight_data)

    # Lancelot vs Mordred
    fight(
        prepared_knights["lancelot"],
        prepared_knights["mordred"],
    )

    # Arthur vs Red Knight
    fight(
        prepared_knights["arthur"],
        prepared_knights["red_knight"],
    )

    return {
        knight["name"]: knight["hp"]
        for knight in prepared_knights.values()
    }
