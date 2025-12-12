from app.knights.knight import Knight


def start_battle(knights: list[tuple[Knight]]) -> dict:
    all_knights = []
    for knights_pair in knights:
        knight1: Knight = knights_pair[0]
        knight2: Knight = knights_pair[1]
        all_knights.append(knight1)
        all_knights.append(knight2)
        knight1.hit_opponent(knight2)
        knight2.hit_opponent(knight1)

    return {
        knight.name: knight.current_hp
        for knight in all_knights
    }
