from app.config import KNIGHTS
from app.models import Knight
from app.engine import fight


def battle(knights_config: dict) -> dict:
    """
    Run the full battle simulation based on the provided configuration.

    Prepares knight objects, executes scheduled duels
    and returns the final HP status for all participants.
    """
    knights = {
        knight: Knight(knights_config[knight])
        for knight in knights_config.keys()
    }

    duels = [("arthur", "red_knight"), ("lancelot", "mordred")]

    for duel in duels:
        fight(knights[duel[0]], knights[duel[1]])
        fight(knights[duel[1]], knights[duel[0]])

    return {knight.name: knight.hp for knight in knights.values()}


if __name__ == "__main__":
    print(battle(KNIGHTS))
