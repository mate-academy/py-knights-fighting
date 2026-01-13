def battle_of_knights(knight_dict: dict, pairs: list) -> dict:
    # battle preparation
    for knight in knight_dict.values():
        knight.battle_preparation()

    # battle
    for battle in pairs:
        knight_dict[battle[0]].hp_calculation(knight_dict[battle[1]])
        knight_dict[battle[1]].hp_calculation(knight_dict[battle[0]])

    return {battle.name: battle.hp for battle in knight_dict.values()}
