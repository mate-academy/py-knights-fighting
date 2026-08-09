from app import knights


def battle(knights_dict: dict) -> dict:
    # creating our dict of dicts with our knights
    battle_dict = {}
    for name, stat in knights_dict.items():
        battle_dict[name] = knights.Knight(
            stat["name"],
            stat["power"],
            stat["hp"],
            stat["armour"],
            stat["weapon"],
            stat["potion"]
        )
    # knights battle each other, and their hp is changing
    knights.Knight.battle(battle_dict["lancelot"], battle_dict["mordred"])
    knights.Knight.battle(battle_dict["arthur"], battle_dict["red_knight"])
    # return result as dict with knight's names and changed hp
    return knights.Knight.battle_result(battle_dict)
