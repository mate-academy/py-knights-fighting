from app.knights.prepare_to_battle import prepare_to_battle


def fight(first_knight: dict, second_knight: dict) -> None:
    prepare_to_battle(first_knight)
    prepare_to_battle(second_knight)

    first_knight["hp"] -= second_knight["power"] - first_knight["protection"]
    second_knight["hp"] -= first_knight["power"] - second_knight["protection"]

    # check if someone fell in battle
    if first_knight["hp"] <= 0:
        first_knight["hp"] = 0

    if second_knight["hp"] <= 0:
        second_knight["hp"] = 0
