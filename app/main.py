import copy
import json
import pprint

from app.calculations.duel import duel
from app.knights.knight import Knight
from app.knights.prepared_knight import PreparedKnight


def battle(knights_config: dict | None = None) -> dict:

    pprint.pprint(knights_config)

    if knights_config is None:
        with open("app/knights/knights.json") as f:
            knights_config = json.load(f)

    if "values" in knights_config:
        knights_list = knights_config["values"]
    else:
        knights_list = list(knights_config.values())

    prepared_knights = [PreparedKnight(Knight(k)) for k in knights_list]

    duel_result_first = duel(
        copy.deepcopy(prepared_knights[0]), copy.deepcopy(prepared_knights[2])
    )
    duel_result_second = duel(
        copy.deepcopy(prepared_knights[1]), copy.deepcopy(prepared_knights[3])
    )

    result = duel_result_first | duel_result_second

    print(result)

    return result
