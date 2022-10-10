from app.knight import get_characteristics


def battle(knights_dict: dict) -> dict:
    knights = get_characteristics(knights_dict)
    results = {"Lancelot": 0, "Artur": 0, "Mordred": 0, "Red Knight": 0}
    for i in range(0, len(knights) // 2):
        sec = i + 2
        knights[i]["hp"] -= knights[sec]["power"] - knights[i]["protection"]
        knights[sec]["hp"] -= knights[i]["power"] - knights[sec]["protection"]
        if knights[i]["hp"] <= 0:
            knights[i]["hp"] = 0
        if knights[sec]["hp"] <= 0:
            knights[sec]["hp"] = 0
        results[knights[i]["name"]] = knights[i]["hp"]
        results[knights[sec]["name"]] = knights[sec]["hp"]
    return results
