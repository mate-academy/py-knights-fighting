from app.dictionary_of_knights import KNIGHTS
from app.create_knights import create_knights
from app.knights import CreateKnights


def battle(dict_new: dict) -> dict[str: int]:
    lancelot = create_knights(dict_new)[0]
    mordred = create_knights(dict_new)[1]
    arthur = create_knights(dict_new)[2]
    red_knight = create_knights(dict_new)[3]

    CreateKnights.sub(lancelot, mordred)
    CreateKnights.sub(mordred, lancelot)
    CreateKnights.sub(arthur, red_knight)
    CreateKnights.sub(red_knight, arthur)

    return print({
            lancelot.name: lancelot.hp,
            arthur.name: arthur.hp,
            mordred.name: mordred.hp,
            red_knight.name: red_knight.hp
        })

battle(KNIGHTS)
