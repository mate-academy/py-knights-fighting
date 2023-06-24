import json

from app.knight import Knight


def battle(knight_data: dict) -> dict:
    data = {
        name: Knight(**information)
        for name, information in knight_data.items()
    }

    # Preparation
    for knight in data.values():
        knight.preparation()

    # Fighting
    data["lancelot"].duel(data["mordred"])
    data["arthur"].duel(data["red_knight"])

    return {
        knight.name: knight.hp
        for knight in data.values()
    }


if __name__ == "__main__":

    with open("knights.json", "r") as file:
        # Result
        print(battle(json.load(file)))
