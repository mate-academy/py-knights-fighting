from app.knight import Knight


def perform_battle(first: Knight, second: Knight) -> None:
    first.hp = max(0, first.hp - (second.power - first.protection))
    second.hp = max(0, second.hp - (first.power - second.protection))
