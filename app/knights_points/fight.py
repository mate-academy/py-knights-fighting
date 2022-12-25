def fight(knights1: dict, knights2: dict) -> dict:

    knights1["hp"] -= knights2["power"] - knights1["protection"]
    knights2["hp"] -= knights1["power"] - knights2["protection"]
    # check if someone fell in battle
    if knights1["hp"] <= 0:
        knights1["hp"] = 0
    if knights2["hp"] <= 0:
        knights2["hp"] = 0
    return knights1, knights2
