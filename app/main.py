from app.builder.knight_builder import build_knight
from app.battle.preparation_to_battle import PreparationToBattle
from app.battle.battle import Battle


def battle(knights: dict) -> dict:
    knights_ready = {}
    for key, value in knights.items():
        knight = build_knight(value)
        knights_ready[key] = (
            PreparationToBattle(knight).preparation_to_battle()
        )

    battle_pairs = [
        ("lancelot", "mordred"),
        ("arthur", "red_knight"),
    ]
    result = {}
    for k1, k2 in battle_pairs:
        outcome = Battle(
            knights_ready[k1], knights_ready[k2]
        ).fight()
        result.update(outcome)

    return result
