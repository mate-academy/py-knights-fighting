# check if knight fell in battle
def check_if_knight_fell(warrior: dict) -> int:
    if warrior["hp"] <= 0:
        warrior["hp"] = 0

    return warrior["hp"]


def count_health_loss(right_fighter: dict, left_fighter: dict) -> int:
    health_loss = right_fighter["power"] - left_fighter["protection"]
    if health_loss < 0:
        health_loss = 0
    return health_loss


def calculate_health_remainder(knight: dict, enemy: dict) -> None:
    knight["hp"] -= count_health_loss(enemy, knight)
