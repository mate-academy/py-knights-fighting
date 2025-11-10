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
    for key_a, key_b in pairings:
        a = knights.get(key_a)
        b = knights.get(key_b)
        if a is None or b is None:
            continue
        a.duel(b)

    return {knight.name: knight.hp for knight in knights.values()}


if __name__ == "__main__":
    results = battle(KNIGHTS)
    print(results)
