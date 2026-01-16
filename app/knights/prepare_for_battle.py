def prepare_knight_for_battle(*knights) -> None:
    for knight in knights:
        knight.get_weapon()
        knight.get_potion()
