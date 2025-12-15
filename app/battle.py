"""
this module count heroes battle result
"""


def heroes_battle(hero_first, hero_second):
    hero_first.hp -= hero_second.power - hero_first.protection
    hero_second.hp -= hero_first.power - hero_second.protection

    # check if someone fell in battle
    if hero_first.hp <= 0:
        hero_first.hp = 0

    if hero_second.hp <= 0:
        hero_second.hp = 0
    return {hero_first.name: hero_first.hp, hero_second.name: hero_second.hp}
