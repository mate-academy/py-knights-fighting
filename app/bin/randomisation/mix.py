import random
from typing import Any

from app.consts.knights import KNIGHTS
from app.consts.parametrs import CHANGABLE


def add_potions() -> dict:
    effect_potion_dict = None
    list_to_add_to_potion = []
    for parametr in CHANGABLE:
        if random.randint(0, 100) < 30:
            list_to_add_to_potion.append(parametr)
    if len(list_to_add_to_potion) > 0:
        effect_potion_dict = dict(name="BlaBlaPotion", effect={
            parametr_name: random.randint(-25, 25)
            for parametr_name in list_to_add_to_potion
        })
    return effect_potion_dict


def change_begin_data(begin_data: dict, key_previous_dict: Any = None) -> None:
    if isinstance(begin_data, dict):
        for key, value in begin_data.items():
            if key in CHANGABLE:
                begin_data[key] = random.randint(50, 100)
            if not isinstance(value, (str, int)):
                if not value and key == "potion":
                    begin_data[key] = add_potions()
                else:
                    change_begin_data(value, key)
    if isinstance(begin_data, list):
        if key_previous_dict == "armour" and len(begin_data) == 0:
            if random.randint(0, 100) < 50:
                for _ in range(1, random.randint(1, 4) + 1):
                    begin_data.append(dict(
                        part="SomeWhere",
                        protection=random.randint(50, 100))
                    )
        else:
            for item in begin_data:
                change_begin_data(item, key_previous_dict)


change_begin_data(KNIGHTS)
