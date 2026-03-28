from .knights_data import KNIGHTS
from .battle import Knight

DEFAULT_PAIRINGS = [
    ("lancelot", "mordred"),
    ("arthur", "red_knight"),
]


def battle(knights_config: dict,
           pairings: list[tuple[str, str]] | None = None
           ) -> dict:

    if pairings is None:
        pairings = DEFAULT_PAIRINGS

    knights: dict = {
        key: Knight(cfg) for key, cfg in knights_config.items()
    }
    for attacker_key, defender_key in pairings:
        attacker = knights.get(attacker_key)
        defender = knights.get(defender_key)
        if attacker is None or defender is None:
            continue
        attacker.duel(defender)

    return {knight.name: knight.hp for knight in knights.values()}


if __name__ == "__main__":
    results = battle(KNIGHTS)
    print(results)
