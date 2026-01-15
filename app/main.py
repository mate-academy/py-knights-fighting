from app.knights.knight import Knight
from app.knights.config import KNIGHTS


def update_health(attacker: Knight, defender: Knight) -> None:
    damage = max(0, attacker.power - defender.protection)
    defender.hp = max(0, defender.hp - damage)


def fight(knight1: Knight, knight2: Knight) -> None:
    while knight1.hp > 0 and knight2.hp > 0:
        update_health(knight1, knight2)
        if knight2.hp <= 0 and not knight2.attempt_resurrection():
            break
        update_health(knight2, knight1)
        if knight1.hp <= 0 and not knight1.attempt_resurrection():
            break


def battle(knights_config: dict) -> dict:
    knights = {name: Knight(config) for name, config in knights_config.items()}

    knight_pairs = [
        ("lancelot", "mordred"),
        ("arthur", "red_knight"),
    ]

    for knight1_name, knight2_name in knight_pairs:
        fight(knights[knight1_name], knights[knight2_name])

    return {
        knights[name].name: knights[name].hp
        for name in knights
    }


def main() -> None:
    battle_results = battle(KNIGHTS)
    print("Battle outcomes:", battle_results)


if __name__ == "__main__":
    main()
