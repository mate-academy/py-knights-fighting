import app.preparing.initialize as init
from app.preparing.knight import Knight
import app.preparing.statistics as stats

results = {}


def battle(team: dict) -> dict:
    for name, knight in team.items():
        if name == "Lancelot":
            Knight.fight(knight, team["Mordred"])
            results["Lancelot"] = knight.hp
            results["Mordred"] = team["Mordred"].hp
        if name == "Arthur":
            Knight.fight(knight, team["Red Knight"])
            results["Arthur"] = knight.hp
            results["Red Knight"] = team["Red Knight"].hp
    return results


print(battle(init.initialize(stats.KNIGHTS)))
