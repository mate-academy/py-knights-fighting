from app.battle.fight import Fight
from app.battle.result import result_of_battle
from app.knights.knights_config import KNIGHTS
from app.knights.dir_of_knights import make_dir_of_knights


def battle(knights_config: dict) -> dict:
    fighters = make_dir_of_knights(knights_config)
    Fight.fight(fighters["lancelot"], fighters["mordred"])
    Fight.fight(fighters["red_knight"], fighters["arthur"])
    return result_of_battle(fighters)


print(battle(KNIGHTS))
