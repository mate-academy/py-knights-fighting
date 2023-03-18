def prepare(
        list_of_participants: list,
        application_dictionary: dict
) -> None:
    hortach = iter(application_dictionary.values())
    for knight in list_of_participants:

        equipment = next(hortach)
        knight.protection = 0

        for specimen in equipment["armour"]:
            knight.protection += specimen["protection"]

        knight.power += equipment["weapon"]["power"]

        if equipment["potion"] is not None:
            potion = equipment["potion"]["effect"]
            if "power" in potion:
                knight.power += potion["power"]
            if "protection" in potion:
                knight.protection += potion["protection"]
            if "hp" in potion:
                knight.hp += potion["hp"]
