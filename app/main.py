from app.heroes.hero_dict import KNIGHTS
from app.fight.fights import fight


def battle(knightsconfig: dict) -> dict:
    fight(knightsconfig)
    return fight(knightsconfig)


print(battle(KNIGHTS))
