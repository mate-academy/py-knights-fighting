from app.unit import Knight


def battle(dict_of_knights: dict) -> dict:
    knights = {
        name: Knight(knight_data)
        for name, knight_data in dict_of_knights.items()
    }

    red_knight = knights.get("red_knight")
    lancelot = knights.get("lancelot")
    arthur = knights.get("arthur")
    mordred = knights.get("mordred")

    first_duel = Knight.duel(lancelot, mordred)
    second_duel = Knight.duel(arthur, red_knight)
    first_duel.update(second_duel)

    return first_duel
