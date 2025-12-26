def put_on(personage: dict) -> dict:
    our_personage = personage.copy()
    our_personage["protection"] = 0
    for armour in personage["armour"]:
        our_personage["protection"] += armour["protection"]

    our_personage["power"] += our_personage["weapon"]["power"]

    if our_personage["potion"] is not None:
        our_p = our_personage["potion"]
        if "power" in our_p["effect"]:
            our_personage["power"] += our_p["effect"]["power"]

        if "protection" in our_p["effect"]:
            our_personage[
                "protection"
            ] += our_p["effect"]["protection"]

        if "hp" in our_p["effect"]:
            our_personage["hp"] += our_personage["potion"]["effect"]["hp"]

    return our_personage


def vs(pers1: dict, pers2: dict) -> dict:
    if pers2["power"] - pers1["protection"] > 0:
        pers1["hp"] -= pers2["power"] - pers1["protection"]
    if pers1["hp"] <= 0:
        pers1["hp"] = 0

    return pers1


def is_alife(personage: dict) -> bool:
    if personage["hp"] > 0:
        return True

    return False
