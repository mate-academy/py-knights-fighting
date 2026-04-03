from app.models.knight import Knight
from app.helpers.battle_logic import fight


def battle(knights_config: dict) -> dict:
    knights = {}

    for key, stats in knights_config.items():
        hp = stats["hp"]
        power = stats["power"] + stats["weapon"]["power"]

        protection = sum(
            part.get("protection", 0)
            for part in stats.get("armour", [])
        )

        potion = stats.get("potion")
        if potion:
            effect = potion.get("effect", {})
            hp += effect.get("hp", 0)
            power += effect.get("power", 0)
            protection += effect.get("protection", 0)

        knights[key] = Knight(stats["name"], hp, power, protection)

    battles = [
        ("lancelot", "mordred"),
        ("arthur", "red_knight")
    ]

    for attacker, defender in battles:
        fight(knights[attacker], knights[defender])

    return {k.name: k.hp for k in knights.values()}
