from .knight import Knights


def duel(hero_1: Knights, hero_2: Knights) -> None:

    hero_1.hp -= hero_2.power - hero_1.protection
    hero_2.hp -= hero_1.power - hero_2.protection

    if hero_1.hp <= 0:
        hero_1.hp = 0

    if hero_2.hp <= 0:
        hero_2.hp = 0
