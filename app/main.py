from actions.hero_manipulations import HeroManipulations
from actions.fight_preparations import FightPreparations
from characters.knights import Knights
from actions.fight import Fight


def battle(heroes: dict) -> dict:

    for hero in heroes.values():
        HeroManipulations.add_to_classes(hero)

    for value in Knights.heroes.values():
        FightPreparations.apply_all(value)

    Fight.fight(Knights.heroes["Lancelot"], Knights.heroes["Mordred"])
    Fight.fight(Knights.heroes["Arthur"], Knights.heroes["Red Knight"])

    print(HeroManipulations.hero_status(Knights))
    return HeroManipulations.hero_status(Knights)
