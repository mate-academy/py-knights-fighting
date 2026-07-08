from app.knights.arthur import Arthur
from app.knights.lancelot import Lancelot
from app.knights.red_knight import RedKnight
from app.knights.mordred import Mordred


def battle(knights: dict) -> None:
    knight_classes = {
        "arthur": Arthur,
        "lancelot": Lancelot,
        "mordred": Mordred,
        "red_knight": RedKnight,
    }

    knight_objects = {
        key: knight_class(**knights[key])
        for key, knight_class in knight_classes.items()
    }

    arthur = knight_objects["arthur"]
    lancelot = knight_objects["lancelot"]
    mordred = knight_objects["mordred"]
    red_knight = knight_objects["red_knight"]

    # BATTLE:

    # 1 Lancelot vs Mordered:
    lancelot.hp -= mordred.powers() - lancelot.protections()
    mordred.hp -= lancelot.powers() - mordred.protections()

    # check if someone fell in battle
    if lancelot.hp <= 0:
        lancelot.hp = 0

    if mordred.hp <= 0:
        mordred.hp = 0

    # 2 Arthur vs Red Knight:
    arthur.hp -= red_knight.powers() - arthur.protections()
    red_knight.hp -= arthur.powers() - red_knight.protections()

    # check if someone fell in battle
    if arthur.hp <= 0:
        arthur.hp = 0

    if red_knight.hp <= 0:
        red_knight.hp = 0

    # Return battle results:
    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }
