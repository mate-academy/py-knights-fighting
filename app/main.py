import json
from app.constants.lists import DUEL_PAIRS
from app.battle_prepare.battle_prepare import battle_prepare
from app.battle_process.battle_process import battle_process


def battle(config: dict) -> dict:
    for knight in config.values():
        battle_prepare(knight)

    for pair in DUEL_PAIRS:
        battle_process(list(pair), config)

    return {
        knight["name"]: knight["hp"]
        for knight in config.values()
    }


with open("app/knights_dict.json") as f:
    data = json.load(f)
    print(battle(data["KNIGHTS"]))
