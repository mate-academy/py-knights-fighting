def calculate_hp(knight_hp: dict, hp: int) -> int:
    if knight_hp is not None:
        if "hp" in knight_hp["effect"]:
            hp += knight_hp["effect"]["hp"]
    return hp
