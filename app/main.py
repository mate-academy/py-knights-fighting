from app.battle_begin.logic_battle import Logic
from app.before_battle.basic_stats import New_Knight
from app.before_battle.extended_stats import ExtendedStats
from app.battle_begin.result import Result


def battle(knightsConfig):
    knights = {}
    for key, value in knightsConfig.items():
        knights[value['name']] = New_Knight(
            value['name'],
            value['power'],
            value['hp'])
        level_up = ExtendedStats(value['armour'],
                                 value['weapon'],
                                 value['potion'])

        knights[value['name']].improve_stats(level_up)

    start_battle = Logic()
    start_battle.ready_set_go(knights)

    return Result.result
