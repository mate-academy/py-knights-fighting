import json
from app.constants.lists import DUEL_PAIRS
from app.battle_prepare.battle_prepare import battle_prepare
from app.battle_process.battle_process import battle_process


def battle(config: dict) -> dict:
    for knight in config:
        battle_prepare(config[knight])

    for pair in DUEL_PAIRS:
        battle_process(list(pair), config)

    return {
        config[knight]["name"]: config[knight]["hp"]
        for knight in config
    }


with open("../app/knights_dict.json") as f:
    data = json.load(f)
    print(battle(data["KNIGHTS"]))
