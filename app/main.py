from app.knights_models import Knight


def fight(first_knight: dict, second_knight: dict) -> None:
    first_knight["hp"] -= second_knight["power"] - first_knight["protection"]
    second_knight["hp"] -= first_knight["power"] - second_knight["protection"]

    if first_knight["hp"] <= 0:
        first_knight["hp"] = 0

    if second_knight["hp"] <= 0:
        second_knight["hp"] = 0


def battle(knights_config: dict) -> dict:

    knights_all = {
        name: Knight.from_dict(data) for name, data in knights_config.items()
    }

    stats = {
        knight.name: {
            "hp": knight.get_hp(),
            "power": knight.get_power(),
            "protection": knight.get_protection(),
        }
        for knight in knights_all.values()
    }

    fight(stats["Lancelot"], stats["Mordred"])
    fight(stats["Arthur"], stats["Red Knight"])

    return {name: data["hp"] for name, data in stats.items()}
