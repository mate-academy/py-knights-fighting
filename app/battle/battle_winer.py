from app.knights.prepare_knight import KnightConfig

def battle_win(first_knight: dict, second_knight: dict) -> dict[str, int]:
    first_knight["hp"] -= second_knight["power"] - first_knight["protection"]
    second_knight["power"] -= first_knight["power"] - second_knight["protection"]

    if first_knight["hp"] <= 0:
        first_knight["hp"] = 0

    if second_knight["hp"] <= 0:
        second_knight["hp"] = 0

    battle_result = {
        first_knight["name"]: first_knight["hp"],
        second_knight["name"]: second_knight["hp"]
    }

    return battle_result
