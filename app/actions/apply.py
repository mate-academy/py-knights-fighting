def apply_armour(player):
    player["protection"] = 0
    for a in player["armour"]:
        player["protection"] += a["protection"]

def apply_weapon(player):
    player["power"] += player["weapon"]["power"]

def apply_potion_if_exist(player):
    if player["potion"]:
        if "power" in player["potion"]["effect"]:
            player["power"] += player["potion"]["effect"]["power"]

        if "protection" in player["potion"]["effect"]:
            player["protection"] += player["potion"]["effect"]["protection"]

        if "hp" in player["potion"]["effect"]:
            player["hp"] += player["potion"]["effect"]["hp"]

def apply_all_for(player):
    apply_armour(player)
    apply_weapon(player)
    apply_potion_if_exist(player)

