from app.character.knights import Knights


def preparation_for_battle(character: Knights) -> Knights:
    Knights.apply_armour(character)
    Knights.apply_weapon(character)
    Knights.apply_potion(character)
    return character
