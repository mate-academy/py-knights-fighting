from app.battle_preparation.initial_data import knights
from app.knights.knight import knight_create
from app.battle_preparation.battle_preparation import knights_power_calculation


def battle(knights_in_dictionary: dict) -> dict:
    game_knights = [knight_create(knights_in_dictionary, knight)
                    for knight in knights_in_dictionary]
    ready_knights = [knights_power_calculation(knight)
                     for knight in game_knights]

    ready_knights[0].hp -= ready_knights[2].power - ready_knights[0].protection
    ready_knights[1].hp -= ready_knights[3].power - ready_knights[1].protection
    ready_knights[2].hp -= ready_knights[0].power - ready_knights[2].protection
    ready_knights[3].hp -= ready_knights[1].power - ready_knights[3].protection

    result = {}
    for knight in ready_knights:
        if knight.hp <= 0:
            knight.hp = 0
        result[knight.name] = knight.hp

    return result


print(battle(knights))
