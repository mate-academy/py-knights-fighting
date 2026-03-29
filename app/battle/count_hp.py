def count_hp(first_person: dict, second_person: dict) -> None:
    first_person["hp"] -= second_person["power"] - first_person["protection"]
    second_person["hp"] -= first_person["power"] - second_person["protection"]

    if first_person["hp"] <= 0:
        first_person["hp"] = 0

    if second_person["hp"] <= 0:
        second_person["hp"] = 0
