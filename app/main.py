from app.change_stats import change_stats


def battle(knights: dict) -> dict:
    warriors = []
    for warrior in knights.values():
        warriors.append(change_stats(warrior))
    for i in range(len(warriors) // 2):
        war1 = warriors[i]
        war2 = warriors[i + len(warriors) // 2]
        war1["hp"] -= (war2["power"] - war1.get("protection", 0))
        war2["hp"] -= (war1["power"] - war2.get("protection", 0))
        if war1["hp"] < 0:
            war1["hp"] = 0
        if war2["hp"] < 0:
            war2["hp"] = 0

    return {war["name"]: war["hp"] for war in warriors}
