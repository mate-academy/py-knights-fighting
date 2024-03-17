from app.KNIGHTS.knights import Knights
from app.KNIGHTS.knight import Knight
from app.fight import fight


def battle(knights_config: dict) -> dict:
    lancelot = Knight(knights_config["lancelot"])
    arthur = Knight(knights_config["arthur"])
    mordred = Knight(knights_config["mordred"])
    red_knight = Knight(knights_config["red_knight"])

    fight(knight1=lancelot, knight2=mordred)
    fight(knight1=arthur, knight2=red_knight)
<<<<<<< HEAD
=======

>>>>>>> 5eb272049e9786edf9f2c2553b6d41b7c96f9af5
    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp
    }


print(battle(Knights))
