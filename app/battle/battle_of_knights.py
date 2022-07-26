def battle_knight(first_knight, second_knight):
    first_knight["hp"] -= second_knight["power"] - first_knight["protection"]
    second_knight["hp"] -= first_knight["power"] - second_knight["protection"]

    # check if someone fell in battle
    if first_knight["hp"] <= 0:
        first_knight["hp"] = 0

    if second_knight["hp"] <= 0:
        second_knight["hp"] = 0


def results(*args):
    return {knight["name"] : knight["hp"] for knight in args}
