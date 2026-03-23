from app.KNIGHTS_list.factory import create_all_knights


def battle(knights_data: dict) -> dict:
    knights = create_all_knights(knights_data)

    lancelot = knights["lancelot"]
    red_knight = knights["red_knight"]
    arthur = knights["arthur"]
    mordred = knights["mordred"]

    lancelot_stats = lancelot.get_stats()
    mordred_stats = mordred.get_stats()
    arthur_stats = arthur.get_stats()
    red_knight_stats = red_knight.get_stats()

    damage_to_1 = mordred_stats["power"] - lancelot_stats["protection"]
    damage_to_2 = lancelot_stats["power"] - mordred_stats["protection"]

    lancelot_stats["hp"] -= damage_to_1
    mordred_stats["hp"] -= damage_to_2
    if lancelot_stats["hp"] <= 0:
        lancelot_stats["hp"] = 0
    if mordred_stats["hp"] <= 0:
        mordred_stats["hp"] = 0

    damage_to_3 = red_knight_stats["power"] - arthur_stats["protection"]
    damage_to_4 = arthur_stats["power"] - red_knight_stats["protection"]

    arthur_stats["hp"] -= damage_to_3
    red_knight_stats["hp"] -= damage_to_4
    if arthur_stats["hp"] <= 0:
        arthur_stats["hp"] = 0
    if red_knight_stats["hp"] <= 0:
        red_knight_stats["hp"] = 0

    return {
        lancelot.name: lancelot_stats["hp"],
        mordred.name: mordred_stats["hp"],
        arthur.name: arthur_stats["hp"],
        red_knight.name: red_knight_stats["hp"],
    }
