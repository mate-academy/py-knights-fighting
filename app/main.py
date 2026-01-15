from app.hero import Hero
from app.knights import KNIGHTS


def battle(config: dict) -> dict:
    if not config:
        config = KNIGHTS

    knights = {}
    for hero_name, hero_data in config.items():
        knight = Hero.create_from_config(config.get(hero_name))
        knight.prepare_to_battle()
        knights[knight.name] = knight

    battles = (("Lancelot", "Mordred"), ("Arthur", "Red Knight"))

    for first_knight, second_knight in battles:
        knights[first_knight].attack(knights[second_knight])
        knights[second_knight].attack(knights[first_knight])

    return {name: knight.hp for name, knight in knights.items()}
