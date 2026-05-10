from app.knights import KNIGHTS
from app.preparing import stats


def check_hp(hp: int) -> int:
    if hp <= 0:
        hp = 0
    return hp


def battle_result(knight1: dict, knight2: dict) -> list:
    knight1["hp"] -= knight2["power"] - knight1["protection"]
    knight1["hp"] = check_hp(knight1["hp"])
    knight2["hp"] -= knight1["power"] - knight2["protection"]
    knight2["hp"] = check_hp(knight2["hp"])
    return [knight1["hp"], knight2["hp"]]


def battle(knights_config: dict) -> dict:
    knights_stats = stats(knights_config)
    result = {}
    battle_pair = [["lancelot", "mordred"], ["arthur", "red_knight"]]
    for item in battle_pair:
        result_battle = \
            battle_result(knights_stats[item[0]], knights_stats[item[1]])
        result[item[0].capitalize()] = result_battle[0]
        result[item[1].capitalize()] = result_battle[1]
    if "Red_knight" in result:
        result["Red Knight"] = result.pop("Red_knight")
    return result
