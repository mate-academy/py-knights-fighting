from app.data import KNIGHTS
from app.models import Knight


def battle(knights_data: dict) -> dict:
    knights = {
        key: Knight(knight_data) for key, knight_data in knights_data.items()
    }

    pairs = [("lancelot", "mordred"), ("arthur", "red_knight")]

    damage_results = {}

    for name1, name2 in pairs:
        h1 = knights[name1]
        h2 = knights[name2]

        damage_to_h2 = h1.power - h2.protection
        damage_to_h1 = h2.power - h1.protection

        damage_results[name1] = damage_to_h1
        damage_results[name2] = damage_to_h2

    final_results = {}
    for key, knight in knights.items():
        damage = damage_results.get(key, 0)
        final_hp = knight.hp - damage
        if final_hp < 0:
            final_hp = 0
        final_results[knight.name] = final_hp

    return final_results


def main() -> None:
    print(battle(KNIGHTS))


if __name__ == "__main__":
    main()
