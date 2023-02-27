from app.knights import CreateKnights


def create_knights(dict_of_knights: dict) -> dict[str, CreateKnights]:
    knights: dict[int] = dict()
    knights_value = {}
    for value_knights in dict_of_knights.values():
        total_power: list[int] = []
        total_protection: list[int] = []
        total_hp: list[int] = []

        total_power.append(value_knights["power"])
        total_power.append(value_knights["weapon"].get("power"))
        total_hp.append(value_knights["hp"])
        for knight_armors in value_knights["armour"]:
            total_protection.append(knight_armors["protection"])
        if value_knights["potion"] is not None:
            total_hp.append(value_knights["potion"]["effect"]["hp"])
            total_power.append(value_knights["potion"]["effect"]["power"])
            total_protection.append(value_knights["potion"]
                                    ["effect"].get("protection", 0))
        knights_value["power"] = sum(total_power)
        knights_value["protection"] = sum(total_protection)
        knights_value["hp"] = sum(total_hp)
        knights[value_knights["name"]] = CreateKnights(
            value_knights["name"],
            knights_value["power"],
            knights_value["protection"],
            knights_value["hp"]
        )

    return knights
