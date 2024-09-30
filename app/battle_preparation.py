def battle(fighter: dict) -> None:
    for person in fighter:
        fighter[person]["protection"] = 0
        fighter[person]["power"] += fighter[person]["weapon"]["power"]
        if fighter[person]["armour"]:
            for elem in fighter[person]["armour"]:
                fighter[person]["protection"] += elem["protection"]
