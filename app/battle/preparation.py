from app.character.knight import Knight


def preparation_for_battle(character: Knight) -> Knight:
    character.apply_armour()
    character.apply_weapon()
    character.apply_potion()
    return character
