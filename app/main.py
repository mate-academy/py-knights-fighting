from actions.hero_manipulations import HeroManipulation
from actions.fight_preparations import FightPreparation
from characters.knight import Knight
from actions.fight import Fight


def battle(heroes: dict) -> dict:

    for hero in heroes.values():
        HeroManipulation.add_to_classes(hero)

    for knight in Knight.heroes.values():
        FightPreparation.apply_all(knight)

    Fight.fight(Knight.heroes["Lancelot"], Knight.heroes["Mordred"])
    Fight.fight(Knight.heroes["Arthur"], Knight.heroes["Red Knight"])

    print(HeroManipulation.hero_status(Knight))
    return HeroManipulation.hero_status(Knight)
