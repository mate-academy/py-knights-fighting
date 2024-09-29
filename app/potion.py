from app.battle_preparation import battle


def potions(fighters: dict) -> None:
    battle(fighters)
    for i in fighters:
        if fighters[i]["potion"]:
            if "power" in fighters[i]["potion"]["effect"]:
                fighters[i]["power"] +=\
                    fighters[i]["potion"]["effect"]["power"]

            if "protection" in fighters[i]["potion"]["effect"]:
                fighters[i]["protection"] +=\
                    fighters[i]["potion"]["effect"]["protection"]

            if "hp" in fighters[i]["potion"]["effect"]:
                fighters[i]["hp"] +=\
                    fighters[i]["potion"]["effect"]["hp"]
