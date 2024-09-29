from app.potion import potions


def fight(fighter: dict) -> dict:
    potions(fighter)
    fighter["lancelot"]["hp"] -= \
        (fighter["mordred"]["power"] - fighter["lancelot"]["protection"])
    fighter["mordred"]["hp"] -= \
        (fighter["lancelot"]["power"] - fighter["mordred"]["protection"])

    if fighter["lancelot"]["hp"] <= 0:
        fighter["lancelot"]["hp"] = 0

    if fighter["mordred"]["hp"] <= 0:
        fighter["mordred"]["hp"] = 0

    fighter["arthur"]["hp"] -=\
        (fighter["red_knight"]["power"] - fighter["arthur"]["protection"])

    fighter["red_knight"]["hp"] -= \
        (fighter["arthur"]["power"] - fighter["red_knight"]["protection"])

    if fighter["arthur"]["hp"] <= 0:
        fighter["arthur"]["hp"] = 0

    if fighter["red_knight"]["hp"] <= 0:
        fighter["red_knight"]["hp"] = 0
    return {
        fighter["lancelot"]["name"]: fighter["lancelot"]["hp"],
        fighter["arthur"]["name"]: fighter["arthur"]["hp"],
        fighter["mordred"]["name"]: fighter["mordred"]["hp"],
        fighter["red_knight"]["name"]: fighter["red_knight"]["hp"],
    }
