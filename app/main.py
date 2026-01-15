import copy
from typing import Any, Dict

from app.knights import KNIGHTS
from persons.lancelot import lancelot
from persons.arthur import arthur
from persons.red_knight import red_knight
from persons.mordred import mordred


def battle(knights_config: Dict[str, Any]) -> Dict[str, Dict]:
    knights = copy.deepcopy(knights_config)

    lancelot_copy = lancelot(copy.deepcopy(knights))
    mordred_copy = mordred(copy.deepcopy(knights))
    arthur_copy = arthur(copy.deepcopy(knights))
    red_knight_copy = red_knight(copy.deepcopy(knights))

    lancelot_copy["hp"] -= mordred_copy["power"] - lancelot_copy["protection"]
    mordred_copy["hp"] -= lancelot_copy["power"] - mordred_copy["protection"]

    for person in (lancelot_copy, mordred_copy):
        if person["hp"] <= 0:
            person["hp"] = 0

    arthur_copy["hp"] -= red_knight_copy["power"] - arthur_copy["protection"]
    red_knight_copy["hp"] -= (arthur_copy["power"]
                              - red_knight_copy["protection"])

    for person in (arthur_copy, red_knight_copy):
        if person["hp"] <= 0:
            person["hp"] = 0

    return {
        i["name"]: i["hp"] for i in (lancelot_copy, arthur_copy,
                                     mordred_copy, red_knight_copy)
    }


print(battle(KNIGHTS))
