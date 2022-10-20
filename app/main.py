from app.knights_fighting.warriors_initialization import heroes_initialization
from app.knights_fighting.knights_config import KNIGHTS


def battle(conf: dict) -> dict:
    """
    Main battle function

    In this function, we arrange fights between heroes
    and display the results of the battles
    :param conf: dict
    :return: dict
    """
    # Save the list of heroes to a variable
    heroes = heroes_initialization(conf)
    # Unpack the list
    lancelot, arthur, mordred, red_knight = heroes

    # battle 1
    lancelot.hp -= mordred.power - lancelot.protection
    mordred.hp -= lancelot.power - mordred.protection

    # check if someone fell in battle
    if lancelot.hp <= 0:
        lancelot.hp = 0

    if mordred.hp <= 0:
        mordred.hp = 0

    # battle 2
    arthur.hp -= red_knight.power - arthur.protection
    red_knight.hp -= arthur.power - red_knight.protection

    # check if someone fell in battle
    if arthur.hp <= 0:
        arthur.hp = 0

    if red_knight.hp <= 0:
        red_knight.hp = 0

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


if __name__ == "__main__":
    print(battle(KNIGHTS))
