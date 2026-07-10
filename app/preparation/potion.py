def get_potion_effect(knight: dict, stat: str) -> int:
    potion = knight.get("potion")
    if not potion:
        return 0
    return potion["effect"].get(stat, 0)
