from app.knights.knight import Knight


def current_stats():
    current_hp_state = {}
    for knight in list(Knight.all_knights.values()):
        current_hp_state[knight.name] = knight.hp
    return current_hp_state
