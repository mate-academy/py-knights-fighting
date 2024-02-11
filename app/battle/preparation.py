from app.character.knight import Knight


def preparation_for_battle(character: Knight) -> Knight:
    Knight.apply_armour(character)
    Knight.apply_weapon(character)
    Knight.apply_potion(character)
    return character
