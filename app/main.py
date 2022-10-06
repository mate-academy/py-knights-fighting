from app.fight.knightConfig import Knights
from app.fight.KnightsConstructor import KNIGHTS


def battle(knights):

    lancelot = Knights(knights["lancelot"])
    arthur = Knights(knights["arthur"])
    mordred = Knights(knights["mordred"])
    red_knight = Knights(knights["red_knight"])

    lancelot.order_determination_winner(mordred)
    arthur.order_determination_winner(red_knight)

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


print(battle(KNIGHTS))
