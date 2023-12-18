from characters.knight import Knight


def battle(heroes: dict) -> dict:
    for hero in heroes.values():
        Knight(hero)

    Knight.fight("Lancelot", "Mordred")
    Knight.fight("Arthur", "Red Knight")

    return Knight.hero_status()
