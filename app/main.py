from app.knights import Knight
import json


def fighting(knight_1: Knight, knight_2: Knight) -> None:
    knight_1.prepare()
    knight_2.prepare()
    knight_1.hp -= knight_2.power - knight_1.protection
    knight_2.hp -= knight_1.power - knight_2.protection

    if knight_1.hp <= 0:
        knight_1.hp = 0
    if knight_2.hp <= 0:
        knight_2.hp = 0


def battle(knights: dict) -> dict:
    lancelot = Knight(*knights.get("lancelot").values())
    arthur = Knight(*knights.get("arthur").values())
    mordred = Knight(*knights.get("mordred").values())
    red_knight = Knight(*knights.get("red_knight").values())

    fighting(lancelot, mordred)
    fighting(arthur, red_knight)

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


with open("app/list_knights.json") as k:
    knights_data = json.load(k)
    print(battle(knights_data))
