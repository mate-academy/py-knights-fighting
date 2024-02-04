from app.versus.versus import versus
from app.versus.versus_result import versus_result
from app.data.knights import KNIGHTS


def battle(knights_config: dict) -> dict:
    knights_stats = {}
    for name, stat in knights_config.items():
        knights_stats[name] = {
            "hp": stat["hp"],
            "power": stat["power"],
            "protection": 0,
        }
        if stat["potion"] is not None:
            for key, value in stat["potion"]["effect"].items():
                knights_stats[name][key] += value
        knights_stats[name]["power"] += stat["weapon"]["power"]
        if len(stat["armour"]) != 0:
            for part in stat["armour"]:
                knights_stats[name]["protection"] += part["protection"]
    # BATTLE:
    versus(knights_stats["lancelot"], knights_stats["mordred"])
    versus(knights_stats["arthur"], knights_stats["red_knight"])
    battle_results = versus_result(knights_stats)
    return battle_results


print(battle(KNIGHTS))
