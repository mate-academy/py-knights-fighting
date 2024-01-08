def fight(first_knight: dict, second_knight: dict) -> None:
    first_knight["hp"] -= second_knight["power"] - first_knight["protection"]
    second_knight["hp"] -= first_knight["power"] - second_knight["protection"]


def check_health(*knights: dict) -> None:
    for knight in knights:
        if knight["hp"] <= 0:
            knight["hp"] = 0
