def apply_potion(knight: object) -> None:
    for effect, count in knight.potion["effect"].items():
        current_value = getattr(knight, effect)
        setattr(knight, effect, current_value + count)
