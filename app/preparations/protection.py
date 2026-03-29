def count_protection(person: dict) -> None:
    person["protection"] = 0
    if isinstance(person["armour"], list):
        for item in person["armour"]:
            person["protection"] += item["protection"]
