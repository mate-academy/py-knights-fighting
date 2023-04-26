def get_armor(knight: dict) -> int:
    protection = 0
    for element in knight["armour"]:
        protection += element["protection"]

    return protection
