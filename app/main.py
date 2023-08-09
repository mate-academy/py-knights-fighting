from app.logic import Knight


def battle(dict_knights: dict) -> dict:

    red_knight = Knight(dict_knights.get("red_knight"))
    lancelot = Knight(dict_knights.get("lancelot"))
    arthur = Knight(dict_knights.get("arthur"))
    mordred = Knight(dict_knights.get("mordred"))

    first_fight = Knight.fight(lancelot, mordred)
    second_fight = Knight.fight(arthur, red_knight)
    first_fight.update(second_fight)

    return first_fight
