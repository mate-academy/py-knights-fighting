from app.knight.knight_class import Knight
from app.data import KNIGHTS


def battle(knights: object) -> dict:
    lancelot = Knight(knights["lancelot"])
    arthur = Knight(knights["arthur"])
    mordred = Knight(knights["mordred"])
    red_knight = Knight(knights["red_knight"])

    # Two battles
    lancelot.versus(mordred)
    arthur.versus(red_knight)

    # I don't understand why this code doesn't work?
    # This is also dict, and it has same objects
    # Maybe, because in this method hp returned as a string?
    # return Knight.list_of_knights

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


print(battle(KNIGHTS))
