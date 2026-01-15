from app.battle_preparations import knight_preparations


def knights_battle(first_knight: dict, second_knight: dict) -> None:
    first_knight["hp"] -= second_knight["power"] - first_knight["protection"]
    second_knight["hp"] -= first_knight["power"] - second_knight["protection"]

    if first_knight["hp"] <= 0:
        first_knight["hp"] = 0

    if second_knight["hp"] <= 0:
        second_knight["hp"] = 0


def battle(knights_config: dict) -> dict:
    knights = [
        knight_preparations(value) for key, value in knights_config.items()
    ]

    knights_battle(*knights[::2][:2])
    knights_battle(*knights[1::2][:2])

    return {knight["name"]: knight["hp"] for knight in knights}
