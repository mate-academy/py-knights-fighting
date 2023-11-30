from actions.hero_manipulations import HeroManipulations
from actions.fight_preparations import FightPreparations
from characters.knight import Knight
from actions.fight import Fight


def battle(heroes: dict) -> dict:

    for hero in heroes.values():
        HeroManipulations.add_to_classes(hero)

    for knight in Knight.heroes.values():
        FightPreparations.apply_all(knight)

    Fight.fight(Knight.heroes["Lancelot"], Knight.heroes["Mordred"])
    Fight.fight(Knight.heroes["Arthur"], Knight.heroes["Red Knight"])

    print(HeroManipulations.hero_status(Knight))
    return HeroManipulations.hero_status(Knight)
