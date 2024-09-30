from app.potion import potions


def fight(fighter: dict) -> dict:
    potions(fighter)
    fighter["lancelot"]["hp"] -= \
        (fighter["mordred"]["power"] - fighter["lancelot"]["protection"])
    fighter["mordred"]["hp"] -= \
        (fighter["lancelot"]["power"] - fighter["mordred"]["protection"])

    fighter["arthur"]["hp"] -=\
        (fighter["red_knight"]["power"] - fighter["arthur"]["protection"])

    fighter["red_knight"]["hp"] -= \
        (fighter["arthur"]["power"] - fighter["red_knight"]["protection"])
    for person in fighter:
        if fighter[person]["hp"] <= 0:
            fighter[person]["hp"] = 0
    return {fighter[elem]["name"] : fighter[elem]["hp"] for elem in fighter}
