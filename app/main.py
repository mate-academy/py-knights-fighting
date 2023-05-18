import json

from app.models import Knight


def create_fighters() -> dict:
    with open("data.json", "r") as data:
        config = json.load(data)
    return config


def battle(configuration: dict) -> dict:
    data = {name: Knight(
        name=configuration[name]["name"],
        human_power=configuration[name]["power"],
        human_hp=configuration[name]["hp"],
        armour=configuration[name]["armour"],
        weapon=configuration[name]["weapon"],
        potion=configuration[name]["potion"],
    ) for name in configuration}

    lancelot = data["lancelot"]
    mordred = data["mordred"]
    arthur = data["arthur"]
    red_knight = data["red_knight"]

    lancelot.human_hp = \
        lancelot.hp() - (mordred.power() - lancelot.protection())
    mordred.human_hp = mordred.hp() - (lancelot.power() - mordred.protection())

    arthur.human_hp = arthur.hp() - (red_knight.power() - arthur.protection())
    red_knight.human_hp = \
        red_knight.hp() - (arthur.power() - red_knight.protection())

    return {
        lancelot.name: lancelot.human_hp,
        arthur.name: arthur.human_hp,
        mordred.name: mordred.human_hp,
        red_knight.name: red_knight.human_hp,
    }
