# from preparation.knights import KNIGHTS
#

def total_stats(KNIGHTS):
    knight_total_stats = KNIGHTS
    for knight in knight_total_stats.values():
        knight["protection"] = 0

        for a in knight["armour"]:
            knight["protection"] += a["protection"]

        knight["power"] += knight["weapon"]["power"]

        if knight["potion"] is not None:
            if "power" in knight["potion"]["effect"]:
                knight["power"] += knight["potion"]["effect"]["power"]

            if "protection" in knight["potion"]["effect"]:
                prot = knight["potion"]["effect"]["protection"]
                knight["protection"] += prot

            if "hp" in knight["potion"]["effect"]:
                knight["hp"] += knight["potion"]["effect"]["hp"]
    return knight_total_stats
