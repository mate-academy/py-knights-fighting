from app.knight import Knight
from app.knight_data import knights_config


def battle(knights_config: dict) -> dict:
    knights = {
        name: Knight(**config)
        for name, config in knights_config.items()
    }

    battle_pairs = [
        ("lancelot", "mordred"),
        ("arthur", "red_knight")
    ]
    for knight1, knight2 in battle_pairs:
        knights[knight1].take_damage(knights[knight2].stats["power"])
        knights[knight2].take_damage(knights[knight1].stats["power"])

    return {knights[k].name: knights[k].stats["hp"] for k in knights}


print(battle(knights_config))
