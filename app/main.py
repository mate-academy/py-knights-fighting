from app.attributes_of_knights.knights import Knight
from app.config.knights import KNIGHTS


def prepare_knights(knights_data: dict) -> dict:
    prepared_knights = {}
    for knight_name, knight_data in knights_data.items():
        knight = Knight(
            name=knight_data["name"],
            power=knight_data["power"],
            hp=knight_data["hp"],
            armour=knight_data["armour"],
            weapon=knight_data["weapon"],
            potion=knight_data["potion"]
        )
        # Apply armour
        knight.protection = knight.calculate_protection()

        # Apply weapon
        knight.power = knight.calculate_power()

        # Apply hp
        knight.hp = knight.calculate_hp()

        prepared_knights[knight_name] = knight

    return prepared_knights


def battle(knights_data: dict) -> dict:
    prepared_knights = prepare_knights(knights_data)

    # -------------------------------------------------------------------------------
    # BATTLE:

    # 1 Lancelot vs Mordred:
    lancelot = prepared_knights["lancelot"]
    mordred = prepared_knights["mordred"]
    lancelot.hp -= mordred.power - lancelot.protection
    mordred.hp -= lancelot.power - mordred.protection

    # Check if someone fell in battle
    if lancelot.hp <= 0:
        lancelot.hp = 0

    if mordred.hp <= 0:
        mordred.hp = 0

    # 2 Arthur vs Red Knight:
    arthur = prepared_knights["arthur"]
    red_knight = prepared_knights["red_knight"]
    arthur.hp -= red_knight.power - arthur.protection
    red_knight.hp -= arthur.power - red_knight.protection

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


print(battle(KNIGHTS))
