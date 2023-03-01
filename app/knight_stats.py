# gives stats to a knight removes BATTLE PREPARATIONS
def knight_stats(knight):
    # instead of creating every knight we are
    # making a function for every knight entry
    knight["protection"] = 0
    for a in knight["armour"]:
        knight["protection"] += a["protection"]

    knight["power"] += knight["weapon"]["power"]
    if knight["potion"] is not None:
        if "power" in knight["potion"]["effect"]:
            knight["power"] += knight["potion"]["effect"]["power"]

        if "protection" in knight["potion"]["effect"]:
            knight["protection"] += knight["potion"]["effect"]["protection"]

        if "hp" in knight["potion"]["effect"]:
            knight["hp"] += knight["potion"]["effect"]["hp"]
    return knight
