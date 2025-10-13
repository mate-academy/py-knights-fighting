from app.knights.knight import Knight
from app.battle.duel import duel
from app.data.knights_data import knights_data


def battle(knights_config: dict) -> dict:
    knights = {}
    for key, data in knights_config.items():
        knights[key] = Knight(
            data["name"],
            data["power"],
            data["hp"],
            data["armour"],
            data["weapon"],
            data["potion"]
        )

    result1 = duel(knights["lancelot"], knights["mordred"])
    result2 = duel(knights["arthur"], knights["red_knight"])

    return {**result1, **result2}


if __name__ == "__main__":
    results = battle(knights_data)
    print("Battle results:", results)
