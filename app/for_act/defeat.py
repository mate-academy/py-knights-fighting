def defeat_check(knight_list: list) -> dict:
    for knight in knight_list:
        if knight["hp"] <= 0:
            knight["hp"] = 0
