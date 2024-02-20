from app.khight_module.khight import Knight
# from app.knight_data import KNIGHTS


def battle(base_knights_config: dict) -> dict:

    lancelot = Knight(knight=base_knights_config["lancelot"])
    arthur = Knight(knight=base_knights_config["arthur"])
    mordred = Knight(knight=base_knights_config["mordred"])
    red_knight = Knight(knight=base_knights_config["red_knight"])

    knights = (lancelot, mordred, arthur, red_knight)
    for obj in knights:
        obj.get_ready_to_battle()

    lancelot.hp -= mordred.power - lancelot.protection
    mordred.hp -= lancelot.power - mordred.protection
    arthur.hp -= red_knight.power - arthur.protection
    red_knight.hp -= arthur.power - red_knight.protection

    for obj in knights:
        if obj.hp <= 0:
            obj.knight_loses_health_to_zero()

    return {knight.name: knight.hp for knight in knights}
