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

    battle1 = Battle(
        knights_ready["lancelot"], knights_ready["mordred"]
    ).fight()
    battle2 = Battle(
        knights_ready["arthur"], knights_ready["red_knight"]
    ).fight()

    result = {}
    result.update(battle1)
    result.update(battle2)
    return result
