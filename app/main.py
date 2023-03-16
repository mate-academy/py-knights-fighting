from app.battle_preparation import battle_preparation
from app.fight import fight
from app.knight_class import create_knight


def battle(knights: dict) -> dict:

    knights = {
        knight["name"]: battle_preparation(create_knight(knight), knight)
        for knight in knights.values()
    }

    lancelot = knights["Lancelot"]
    arthur = knights["Artur"]
    mordred = knights["Mordred"]
    red_knight = knights["Red Knight"]

    fight(lancelot, mordred)
    fight(mordred, lancelot)
    fight(arthur, red_knight)
    fight(red_knight, arthur)

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp
    }
