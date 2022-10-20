from app.knights import Knights


def battle(dict_of_knights) -> dict:
    list_of_knights = Knights.knight_config(dict_of_knights)

    lancelot = list_of_knights["Lancelot"]
    arthur = list_of_knights["Artur"]
    mordred = list_of_knights["Mordred"]
    red_knight = list_of_knights["Red Knight"]
    lancelot.hp -= mordred.power - lancelot.protection
    mordred.hp -= lancelot.power - mordred.protection
    arthur.hp -= red_knight.power - arthur.protection
    red_knight.hp -= arthur.power - red_knight.protectio

    for warrior, stats in list_of_knights.items():
        if stats.hp <= 0:
            stats.hp = 0
        list_of_knights[warrior] = stats.hp
    return list_of_knights
