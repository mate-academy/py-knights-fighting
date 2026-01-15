import json

from app.models import Knight


def create_fighters() -> dict:
    with open("data.json", "r") as data:
        config = json.load(data)
    return config


def duel(first: Knight, second: Knight) -> None:
    first.human_hp = first.hp() - (second.power() - first.protection())
    second.human_hp = second.hp() - (first.power() - second.protection())


def battle(configuration: dict) -> dict:
    data = {name: Knight(value) for name, value in configuration.items()}

    lancelot = data["lancelot"]
    mordred = data["mordred"]
    arthur = data["arthur"]
    red_knight = data["red_knight"]

    duel(lancelot, mordred)
    duel(arthur, red_knight)

    return {
        lancelot.name: lancelot.human_hp,
        arthur.name: arthur.human_hp,
        mordred.name: mordred.human_hp,
        red_knight.name: red_knight.human_hp,
    }
