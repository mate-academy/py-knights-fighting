from app.initiate_knight import initiate_the_knight


def duel_of_knights(first_knight: dict, second_knight: dict) -> dict:
    first_knight = initiate_the_knight(first_knight)
    second_knight = initiate_the_knight(second_knight)
    first_knight.hp -= second_knight.power - first_knight.protection
    second_knight.hp -= first_knight.power - second_knight.protection
    knights = [first_knight, second_knight]
    for knight in knights:
        if knight.hp <= 0:
            knight.hp = 0
    return {
        knight.name: knight.hp for knight in knights
    }
