from app.knight import get_characteristics


def battle(knights_dict: dict) -> dict:
    knights = get_characteristics(knights_dict)
    results = {"Lancelot": 0, "Artur": 0, "Mordred": 0, "Red Knight": 0}
    for index in range(0, len(knights) // 2):
        index2 = index + 2
        knights[index]["hp"] -= (knights[index2]["power"]
                                 - knights[index]["protect"])
        knights[index2]["hp"] -= (knights[index]["power"]
                                  - knights[index2]["protect"])
        if knights[index]["hp"] <= 0:
            knights[index]["hp"] = 0
        if knights[index2]["hp"] <= 0:
            knights[index2]["hp"] = 0
        results[knights[index]["name"]] = knights[index]["hp"]
        results[knights[index2]["name"]] = knights[index2]["hp"]
    return results
