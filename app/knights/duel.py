def duel(hero_1, hero_2):

    hero_1.hp -= hero_2.power - hero_1.protection
    hero_2.hp -= hero_1.power - hero_2.protection

    if hero_1.hp <= 0:
        hero_1.hp = 0

    if hero_2.hp <= 0:
        hero_2.hp = 0
