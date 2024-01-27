from app.KNIGHTS.KNIGHTS import KNIGHTS


def apply_attributes(knight: dict) -> None:
    # Apply armour
    knight["protection"] = sum(a["protection"] for a in knight["armour"])

    # Apply weapon
    knight["power"] += knight["weapon"]["power"]

    # Apply potion if exists
    if knight["potion"] is not None:
        potion_effect = knight["potion"]["effect"]
        knight["power"] += potion_effect.get("power", 0)
        knight["protection"] += potion_effect.get("protection", 0)
        knight["hp"] += potion_effect.get("hp", 0)


def battle(knights: dict) -> dict:
    for knight_name, knight in knights.items():
        apply_attributes(knight)
    knights["lancelot"]["hp"] -= (knights["mordred"]["power"]
                                  - knights["lancelot"]["protection"])
    knights["mordred"]["hp"] -= (knights["lancelot"]["power"]
                                 - knights["mordred"]["protection"])
    knights["lancelot"]["hp"] = max(0, knights["lancelot"]["hp"])
    knights["mordred"]["hp"] = max(0, knights["mordred"]["hp"])
    knights["arthur"]["hp"] -= (knights["red_knight"]["power"]
                                - knights["arthur"]["protection"])
    knights["red_knight"]["hp"] -= (knights["arthur"]["power"]
                                    - knights["red_knight"]["protection"])
    knights["arthur"]["hp"] = max(0, knights["arthur"]["hp"])
    knights["red_knight"]["hp"] = max(0, knights["red_knight"]["hp"])
    return {
        knights["lancelot"]["name"]: knights["lancelot"]["hp"],
        knights["arthur"]["name"]: knights["arthur"]["hp"],
        knights["mordred"]["name"]: knights["mordred"]["hp"],
        knights["red_knight"]["name"]: knights["red_knight"]["hp"],
    }


print(battle(KNIGHTS))
