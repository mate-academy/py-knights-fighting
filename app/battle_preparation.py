def battle(fighter: dict) -> None:
    for i in fighter:
        fighter[i]["protection"] = 0
        fighter[i]["power"] += fighter[i]["weapon"]["power"]
        if fighter[i]["armour"]:
            for j in fighter[i]["armour"]:
                fighter[i]["protection"] += j["protection"]
