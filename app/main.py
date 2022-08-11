from app.battle import Battle
from app.heroes import KNIGHTS


def battle(knights: dict):

    fight = Battle(knights)

    fight.battle("Lancelot", "Mordred")
    fight.battle("Artur", "Red Knight")

    return {
        "Lancelot": fight.heroes["Lancelot"].hp,
        "Artur": fight.heroes["Artur"].hp,
        "Mordred": fight.heroes["Mordred"].hp,
        "Red Knight": fight.heroes["Red Knight"].hp,
    }


print(battle(KNIGHTS))
