from app.builder.knight_builder import build_knight
from app.battle.preparation_to_battle import PreparationToBattle
from app.battle.battle import Battle


def battle(knights: dict) -> dict:
    lancelot = build_knight(knights["lancelot"])
    arthur = build_knight(knights["arthur"])
    mordred = build_knight(knights["mordred"])
    red_knight = build_knight(knights["red_knight"])

    lancelot_ready = PreparationToBattle(lancelot).preparation_to_battle()
    arthur_ready = PreparationToBattle(arthur).preparation_to_battle()
    mordred_ready = PreparationToBattle(mordred).preparation_to_battle()
    red_knight_ready = PreparationToBattle(red_knight).preparation_to_battle()

    battle1 = Battle(lancelot_ready, mordred_ready).fight()
    battle2 = Battle(arthur_ready, red_knight_ready).fight()

    result = {}
    result.update(battle1)
    result.update(battle2)
    return result
