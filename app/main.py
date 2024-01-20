from app.knight import Knight
from app.knights import KNIGHTS


def create_knight(data: dict) -> Knight:
    return Knight(**data)


def battle(knights_config: dict[dict]) -> dict:
    knights = []

    for knight_data in knights_config.values():
        knights.append(create_knight(knight_data))

    lancelot, arthur, mordred, red_knight = knights

    lancelot.hp -= mordred.power - lancelot.protection
    mordred.hp -= lancelot.power - mordred.protection

    lancelot.hp = max(0, lancelot.hp)
    mordred.hp = max(0, mordred.hp)

    arthur.hp -= red_knight.power - arthur.protection
    red_knight.hp -= arthur.power - red_knight.protection

    arthur.hp = max(0, arthur.hp)
    red_knight.hp = max(0, red_knight.hp)

    return {knight.name: knight.hp for knight in knights}


print(battle(KNIGHTS))
