from app.data import knights_dict


def applying(knight):
    for armour in knight["armour"]:
        knight["protection"] += armour["protection"]

    knight["power"] += knight["weapon"]["power"]

    if knight["potion"] is not None:
        if "power" in knight["potion"]["effect"]:
            knight["power"] += knight["potion"]["effect"]["power"]

        if "protection" in knight["potion"]["effect"]:
            knight["protection"] += knight["potion"]["effect"]["protection"]

        if "hp" in knight["potion"]["effect"]:
            knight["hp"] += knight["potion"]["effect"]["hp"]


def battle(knights_):
    knights = lancelot, arthur, mordred, red_knight = [
        knight for knight in knights_.values()
    ]

    for knight in knights:
        knight["protection"] = 0
        applying(knight)

    lancelot["hp"] -= mordred["power"] - lancelot["protection"]
    mordred["hp"] -= lancelot["power"] - mordred["protection"]
    arthur["hp"] -= red_knight["power"] - arthur["protection"]
    red_knight["hp"] -= arthur["power"] - red_knight["protection"]

    for knight in knights:
        if knight["hp"] < 0:
            knight["hp"] = 0

    return {knight["name"]: knight["hp"] for knight in knights}


print(battle(knights_dict))
