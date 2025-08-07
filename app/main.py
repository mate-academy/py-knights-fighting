# app/main.py

from app.constants import KNIGHTS
from app.knight import Knight


def _perform_duel(knight1: Knight, knight2: Knight) -> None:
    """Each knight attacks the other once."""
    knight1.take_damage(knight2.power)
    knight2.take_damage(knight1.power)


def battle(knights_config: dict) -> dict:
    # Instantiate all knights from config
    knights = {key: Knight(data) for key, data in knights_config.items()}

    # Perform duels
    _perform_duel(knights["lancelot"], knights["mordred"])
    _perform_duel(knights["arthur"], knights["red_knight"])

    # Return remaining HP for each knight
    return {knight.name: knight.hp for knight in knights.values()}


if __name__ == "__main__":
    results = battle(KNIGHTS)
    print(results)
