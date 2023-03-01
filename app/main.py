from app.championship import Championship
from app.heroes import KNIGHTS


def battle(knights: dict):
    championship = Championship(knights)

    championship.battle("Lancelot", "Mordred")
    championship.battle("Artur", "Red Knight")

    return {
        "Lancelot": championship.heroes["Lancelot"].hp,
        "Artur": championship.heroes["Artur"].hp,
        "Mordred": championship.heroes["Mordred"].hp,
        "Red Knight": championship.heroes["Red Knight"].hp,
    }


print(battle(KNIGHTS))
