from app.heroes.hero_dict import KNIGHTS
from app.fight.fights import fight


def battle(knightsconfig: dict) -> dict:
    return fight(knightsconfig)


print(battle(KNIGHTS))
