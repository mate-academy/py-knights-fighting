def knight_stat(knight: dict) -> dict:
    hp = 0
    power = 0
    hp += knight["hp"]
    power += knight["power"] + knight["weapon"]["power"]
    for armour in knight["armour"]:
        hp += armour["protection"]
    if knight["potion"] is not None:
        for potion in knight["potion"]["effect"]:
            if potion == "power":
                power += knight["potion"]["effect"]["power"]
            else:
                hp += knight["potion"]["effect"][potion]
    return {"hp": hp, "power": power}
