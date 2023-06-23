import json

from app.models.knight import Knight
from app.models.tool_model import Armour, Potion, Weapon


def configurate_data(data: dict) -> dict:
    return {
        name: Knight(
            name=knight["name"],
            power=knight["power"],
            hp=knight["hp"],
            armour=[
                Armour(
                    part=arm["part"],
                    protection=arm["protection"])
                for arm in knight["armour"]
            ],
            weapon=Weapon(
                name=knight["weapon"]["name"],
                power=knight["weapon"]["power"]
            ),
            potion=Potion(
                name=knight["potion"]["name"],
                effect=knight["potion"]["effect"]
            ) if knight.get("potion") else None
        ) for name, knight in data.items()
    }


def battle(knight_data: dict) -> dict:
    data = configurate_data(knight_data)
    # Preparation
    for knight in data.values():
        knight.preparation()

    # Fighting
    data["lancelot"] -= data["mordred"]
    data["arthur"] -= data["red_knight"]

    return {
        value.name: value.hp for value in data.values()
    }


if __name__ == "__main__":

    with open("knights.json", "r") as file:
        # Result
        print(battle(json.load(file)))
