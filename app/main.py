from app.knight import Knight

"""
We have also interactive mode ready to use.
To try it, please, run "my_app/interactive.py"
"""


def battle(knights_config: dict) -> dict:
    list_of_knights = Knight.creation(knights_config=knights_config)
    lancelot = list_of_knights[0]
    arthur = list_of_knights[1]
    mordred = list_of_knights[2]
    red_knight = list_of_knights[3]

    lancelot.hp -= mordred.power - lancelot.protection
    mordred.hp -= lancelot.power - mordred.protection

    arthur.hp -= red_knight.power - arthur.protection
    red_knight.hp -= arthur.power - red_knight.protection

    for knight in list_of_knights:
        if knight.hp < 0:
            knight.hp = 0

    return {
        knight.name: knight.hp for knight in list_of_knights
    }
