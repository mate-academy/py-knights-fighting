from app.knights import Knight
import json


def battle(knights: dict) -> dict:
    lancelot = Knight(*knights.get("lancelot").values())
    arthur = Knight(*knights.get("arthur").values())
    mordred = Knight(*knights.get("mordred").values())
    red_knight = Knight(*knights.get("red_knight").values())

    lancelot.fighting(mordred)
    arthur.fighting(red_knight)

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


with open("app/list_knights.json") as k:
    knights_data = json.load(k)
    print(battle(knights_data))
