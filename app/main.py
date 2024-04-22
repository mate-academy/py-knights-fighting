from Knights_attributes import KNIGHTS


def prepare_knight(knight):
    knight["protection"] = sum(a["protection"] for a in knight["armour"])
    knight["power"] += knight["weapon"]["power"]
    if knight["potion"]:
        for effect in ["power", "protection", "hp"]:
            if effect in knight["potion"]["effect"]:
                knight[effect] += knight["potion"]["effect"][effect]


def battle(knights_config):
    for knight_name, knight in knights_config.items():
        prepare_knight(knight)

    lancelot = knights_config["lancelot"]
    mordred = knights_config["mordred"]
    arthur = knights_config["arthur"]
    red_knight = knights_config["red_knight"]

    lancelot["hp"] -= mordred["power"] - lancelot["protection"]
    mordred["hp"] -= lancelot["power"] - mordred["protection"]

    arthur["hp"] -= red_knight["power"] - arthur["protection"]
    red_knight["hp"] -= arthur["power"] - red_knight["protection"]

    for knight in [lancelot, mordred, arthur, red_knight]:
        knight["hp"] = max(0, knight["hp"])

    return {knight["name"]: knight["hp"] for knight in [lancelot, arthur, mordred, red_knight]}


print(battle(KNIGHTS))
