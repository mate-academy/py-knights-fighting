def prepare(
        list_of_participants: list,
        application_dictionary: dict
) -> None:
    hortach = iter(application_dictionary.values())
    for knight in list_of_participants:

        equipment = next(hortach)
        knight.protection = 0

        for specimen in equipment.get("armour", []):
            knight.protection += specimen.get("protection")

        knight.power += equipment.get("weapon").get("power")

        if equipment.get("potion") is not None:
            potion = equipment.get("potion").get("effect")
            if "power" in potion:
                knight.power += potion.get("power")
            if "protection" in potion:
                knight.protection += potion.get("protection")
            if "hp" in potion:
                knight.hp += potion.get("hp")
