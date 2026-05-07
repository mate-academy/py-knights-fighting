from collections.abc import Iterable


def health_check(knight: dict) -> None:
    if knight["hp"] <= 0:
        knight["hp"] = 0


def fighting(first_knight: dict, second_knight: dict) -> None:
    first_knight["hp"] -= second_knight["power"] - first_knight["protection"]
    second_knight["hp"] -= first_knight["power"] - second_knight["protection"]

    for knight in [first_knight, second_knight]:
        health_check(knight)


def battle_results(knights: Iterable[dict]) -> dict:
    return {knight["name"]: knight["hp"] for knight in knights}
