from Knights_data.Stats import KnightStats
from Knights_data.Knights import Knight
from Knights_data.unformated import KNIGHTS


def battle(knightsconfig: dict) -> dict:
    knights = {}
    for stats in knightsconfig.values():
        knight = KnightStats(stats["name"], stats["power"], stats["hp"],
                             stats["armour"], stats["weapon"], stats["potion"])
        knights[stats["name"]] = Knight(knight)
    knights["Lancelot"] - knights["Mordred"]
    knights["Artur"] - knights["Red Knight"]
    print(knights)
    return {name: stats.hp for name, stats in knights.items()}


print(battle(KNIGHTS))
