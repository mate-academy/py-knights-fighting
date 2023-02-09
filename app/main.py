from app.characters.knight import Knight
from app.actions import actions


def battle(knights_config: dict[str, dict]) -> dict[str, int]:
    battle_members = {knight_name: Knight(knight_info)
                      for knight_name, knight_info in knights_config.items()}

    pairs = [[battle_members["lancelot"], battle_members["mordred"]],
             [battle_members["arthur"], battle_members["red_knight"]]]

    [actions.duel(pair) for pair in pairs]

    return {knight.name: knight.hp for knight in battle_members.values()}
