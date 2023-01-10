from knight import Knight


def battle_preparation(knight: Knight) -> None:
    """Function prepare knight for a battle"""
    knight.get_armour()
    knight.get_weapon()
    knight.get_potion()


def duel(knight_1: Knight, knight_2: Knight) -> None:
    """
    Function imitates a duel between two knights
    and changes knight`s health_points by results
    """
    knight_1.hp += (knight_1.protection - knight_2.power)
    knight_2.hp += (knight_2.protection - knight_1.power)


def check_if_fell(knight: Knight) -> None:
    """Function checks if knight fell"""
    if knight.hp <= 0:
        knight.hp = 0


def battle_results(knights: dict) -> dict:
    """Function returns a dictionary with results of a knights battle"""
    return {knight.real_name: knight.hp for knight in knights}


def battle(knights: dict) -> dict:

    participants = {
        knight: Knight(knight, knights)
        for knight in knights
    }

    for participant in participants.values():
        battle_preparation(participant)

    duel(participants["lancelot"], participants["mordred"])
    duel(participants["arthur"], participants["red_knight"])

    for participant in participants.values():
        check_if_fell(participant)

    return battle_results(participants.values())

# 1 Lancelot vs Mordred:
# 2 Arthur vs Red Knight:
# Return battle results:
# {'Lancelot': 0, 'Artur': 30, 'Mordred': 35, 'Red Knight': 5}
