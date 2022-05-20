from knight.knight import Knight
from battle.battle import Battle


def battle(knights_config):

    knights = [Knight(knights_config[knight])
               for knight in knights_config.keys()]

    for k in range(0, len(knights) - 2):
        battle_result = Battle(knights[k], knights[k + 2])
        battle_result.attack()

    battle_results = {}

    for k in range(0, len(knights) - 2):
        battle_results.update({knights[k].name: knights[k].hp})
        battle_results.update({knights[k + 2].name: knights[k + 2].hp})

    return battle_results
