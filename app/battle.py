def check(fisrt: dict, second: dict) -> None:
    fisrt["hp"] -= second["power"] - fisrt["protection"]
    second["hp"] -= fisrt["power"] - second["protection"]

    if fisrt["hp"] <= 0:
        fisrt["hp"] = 0

    if second["hp"] <= 0:
        second["hp"] = 0
