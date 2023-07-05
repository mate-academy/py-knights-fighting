from app.modules.battle import Battleground
from app.modules.knights import Knight


def battle(knightsConfig: dict) -> dict | str:
    knights = []

    # transforming input to Knight
    for k in knightsConfig:
        knights.append(Knight(k))

    # LET THE BATTLE BEGIN
    if len(knights) % 2 == 0:
        for index in range(0, len(knights)-2, 2):
            Battleground.fight(knights[index], knights[index+2])
    else:
        return "Not enough knights this year"

    return {knights[index].name: knights[index].hp for index in range(len(knights))}
