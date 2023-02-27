from app.dictionary_of_knights import KNIGHTS
from app.create_knights import create_knights
from app.knights import CreateKnights


def battle(dict_of_knights: dict) -> dict[str: int]:
    knights: dict[str, CreateKnights] = create_knights(dict_of_knights)

    lancelot: CreateKnights = knights["Lancelot"]
    mordred: CreateKnights = knights["Mordred"]
    arthur: CreateKnights = knights["Artur"]
    red_knight: CreateKnights = knights["Red Knight"]

    CreateKnights.fight(lancelot, mordred)
    CreateKnights.fight(mordred, lancelot)
    CreateKnights.fight(arthur, red_knight)
    CreateKnights.fight(red_knight, arthur)

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp
    }


battle(KNIGHTS)
