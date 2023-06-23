from app.unit import Knight


def battle(dict_of_knigths: dict) -> dict:
    red_knight = Knight(dict_of_knigths.get("red_knight"))
    lancelot = Knight(dict_of_knigths.get("lancelot"))
    arthur = Knight(dict_of_knigths.get("arthur"))
    mordred = Knight(dict_of_knigths.get("mordred"))

    first_duel = Knight.duel(lancelot, mordred)
    second_duel = Knight.duel(arthur, red_knight)
    first_duel.update(second_duel)

    return first_duel
