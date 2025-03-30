from .config import KNIGHTS
from app.models.knights import Knight
from .arena.arena import Arena


def battle(knights_config: dict[str, dict]) -> dict[str, int]:
    battles = [
        ("lancelot", "mordred"),
        ("arthur", "red_knight")
    ]

    results = {}

    for knight1_id, knight2_id in battles:
        knight1 = Knight(knights_config[knight1_id])
        knight2 = Knight(knights_config[knight2_id])
        arena = Arena(knight1, knight2)
        # Отримуємо результати одного бою
        arena_result = arena.fight()

        # Оновлюємо підсумковий словник фінальними значеннями HP лицарів
        results[knight1.name] = arena_result[knight1.name]
        results[knight2.name] = arena_result[knight2.name]

    return results


if __name__ == "__main__":
    battle_results = battle(KNIGHTS)
    print(battle_results)
