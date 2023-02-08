from Knights_data.Stats import KnightStats
from Knights_data.Knights import Knight
from Knights_data.unformated import KNIGHTS


def battle(knightsconfig: dict) -> dict:
    knights = {}
    for stats in knightsconfig.values():
        knight = KnightStats(stats["name"], stats["power"], stats["hp"],
                             stats["armour"], stats["weapon"], stats["potion"])
        KnightStats.potion(KnightStats.knights[stats["name"]])
        knights[stats["name"]] = Knight(knight)
    knightsconfig = knights
    knightsconfig["Lancelot"] - knightsconfig["Mordred"]
    knightsconfig["Artur"] - knightsconfig["Red Knight"]
    # print(knightsConfig)
    return {name: stats.hp for name, stats in knightsconfig.items()}


print(battle(KNIGHTS))
