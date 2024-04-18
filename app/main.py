from app.knights.heroes import init_hero
from app.knights.data import KNIGHTS


def battle(knights_config: dict) -> dict:
    heroes = init_hero(knights_config)
    pairs = [
        [
            heroes[i], heroes[len(heroes) // 2 + i]
        ] for i in range(len(heroes) // 2)
    ]
    if len(heroes) % 2 != 0:
        heroes.remove(heroes[-1])
        print("The last participant is eliminated because he has no opponent.")
    for opponents in pairs:
        opponents[0].hp -= opponents[1].power - opponents[0].protection
        opponents[1].hp -= opponents[0].power - opponents[1].protection
        for opponent in opponents:
            if opponent.hp <= 0:
                opponent.hp = 0
    return {hero.name: hero.hp for hero in heroes}


print(battle(KNIGHTS))
