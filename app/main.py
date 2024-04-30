from app.battle_preparations import knight_preparations


def knights_battle(first_knight: dict, second_knight: dict) -> None:
    first_knight["hp"] -= second_knight["power"] - first_knight["protection"]
    second_knight["hp"] -= first_knight["power"] - second_knight["protection"]

    if first_knight["hp"] <= 0:
        first_knight["hp"] = 0

    if second_knight["hp"] <= 0:
        second_knight["hp"] = 0


def battle(knights_config: dict) -> dict:
    knights = {
        key: knight_preparations(value)
        for key, value in knights_config.items()
    }

    knights_battle(knights["lancelot"], knights["mordred"])
    knights_battle(knights["arthur"], knights["red_knight"])

    return {
        knight_name.replace("_", " ").title(): knight_stat["hp"]
        for knight_name, knight_stat in knights.items()
    }
