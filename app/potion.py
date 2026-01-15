from app.battle_preparation import battle


def potions(fighters: dict) -> None:
    battle(fighters)
    for person in fighters:
        if fighters[person]["potion"]:
            if "power" in fighters[person]["potion"]["effect"]:
                fighters[person]["power"] +=\
                    fighters[person]["potion"]["effect"]["power"]

            if "protection" in fighters[person]["potion"]["effect"]:
                fighters[person]["protection"] +=\
                    fighters[person]["potion"]["effect"]["protection"]

            if "hp" in fighters[person]["potion"]["effect"]:
                fighters[person]["hp"] +=\
                    fighters[person]["potion"]["effect"]["hp"]
