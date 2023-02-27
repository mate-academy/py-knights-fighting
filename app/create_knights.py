from app.knights import Knights


def create_knights(dict_of_knights: dict) -> dict[str, Knights]:
    knights: dict[int] = dict()
    knights_value = {}
    for value_knights in dict_of_knights.values():
        total_power: int = 0
        total_protection: int = 0
        total_hp: int = 0

        total_power += (value_knights["power"])
        total_power += (value_knights["weapon"].get("power"))
        total_hp += (value_knights["hp"])
        for knight_armors in value_knights["armour"]:
            total_protection += (knight_armors["protection"])
        if value_knights["potion"] is not None:
            total_hp += (value_knights["potion"]["effect"]["hp"])
            total_power += (value_knights["potion"]["effect"]["power"])
            total_protection += (value_knights["potion"]
                                 ["effect"].get("protection", 0))
        knights_value["power"] = total_power
        knights_value["protection"] = total_protection
        knights_value["hp"] = total_hp
        knights[value_knights["name"]] = Knights(
            value_knights["name"],
            knights_value["power"],
            knights_value["protection"],
            knights_value["hp"]
        )

    return knights
