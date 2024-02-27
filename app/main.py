from app.knight.knight import Knight
from app.knight.knight_konfig import KNIGHTS


def battle(knights_config: dict) -> dict:
    # create knights
    knights = [Knight(knight["name"],
                      knight["power"],
                      knight["hp"],
                      knight["armour"],
                      knight["weapon"],
                      knight["potion"])
               for knight in knights_config.values()]

    # prepare for battle
    for knight in knights:
        knight.prepare_to_battle()

    # Lancelot vs Mordred
    knights[0].fight(knights[2])

    # Arthur vs Red Knight
    knights[1].fight(knights[3])

    # return knight`s name and health point
    return {knight.name: knight.hp for knight in knights}


print(battle(KNIGHTS))
