from app.format_knight import format


def battle(knights: dict) -> dict:

    format_knights = format(knights)
    print(format_knights)

    knight_names = list(format_knights.keys())
    result = {}

    for index in range(0, len(knight_names), 2):
        if index + 1 < len(knight_names):
            knight_one_name = knight_names[index]
            knight_two_name = knight_names[index + 1]

            knight_one = format_knights[knight_one_name]
            knight_two = format_knights[knight_two_name]

            knight_one["hp"] -= knight_two["power"] - knight_one["protection"]
            knight_two["hp"] -= knight_one["power"] - knight_two["protection"]

            knight_one["hp"] = max(0, knight_one["hp"])
            knight_two["hp"] = max(0, knight_two["hp"])

            result[knight_one_name] = knight_one["hp"]
            result[knight_two_name] = knight_two["hp"]

    return result
