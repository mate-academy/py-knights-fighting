from app.potion import potions
from app.fight import fights


def fight(fighter: dict) -> dict:
    potions(fighter)
    fights(fighter["lancelot"], fighter["mordred"])
    fights(fighter["red_knight"], fighter["arthur"])
    for person in fighter:
        if fighter[person]["hp"] <= 0:
            fighter[person]["hp"] = 0
    return {fighter[elem]["name"] : fighter[elem]["hp"] for elem in fighter}
