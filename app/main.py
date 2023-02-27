from app.create_knights import create_knights
from app.dictionary_of_knights import KNIGHTS
from app.knights import Knights


def battle(dict_of_knights: dict) -> dict[str: int]:
    knights: dict[str, Knights] = create_knights(dict_of_knights)

    lancelot: Knights = knights["Lancelot"]
    mordred: Knights = knights["Mordred"]
    arthur: Knights = knights["Artur"]
    red_knight: Knights = knights["Red Knight"]

    Knights.fight(lancelot, mordred)
    Knights.fight(mordred, lancelot)
    Knights.fight(arthur, red_knight)
    Knights.fight(red_knight, arthur)

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp
    }


battle(KNIGHTS)
