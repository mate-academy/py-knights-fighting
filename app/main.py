from Knights_data.Knights import Knight
from Knights_data.unformated import KNIGHTS


def battle(knightsconfig: dict) -> dict:
    knights = {}
    for stats in knightsconfig.values():
        knights[stats["name"]] = Knight(stats["name"], stats["power"],
                                        stats["hp"], stats["armour"],
                                        stats["weapon"], stats["potion"])
    knights["Lancelot"] - knights["Mordred"]
    knights["Artur"] - knights["Red Knight"]
    return {name: stats.hp for name, stats in knights.items()}


print(battle(KNIGHTS))
