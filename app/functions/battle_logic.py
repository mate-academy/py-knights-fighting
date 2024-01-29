from app.functions.apply_atributes import apply_attributes


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
