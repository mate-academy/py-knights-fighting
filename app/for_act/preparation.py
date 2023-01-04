from typing import Callable


def apply_armour(fighter: list[dict]) -> None:
    fighter["protection"] = 0
    for armour in fighter["armour"]:
        fighter["protection"] += armour["protection"]


def apply_weapon(fighter: list[dict]) -> None:
    fighter["power"] += fighter["weapon"]["power"]


def apply_potion(fighter: list[dict]) -> None:
    if fighter["potion"] is not None:
        for element in fighter["potion"]["effect"]:
            fighter[element] += fighter["potion"]["effect"][element]


def prepare_to_the_battle(fighter: list[dict]) -> Callable:
    apply_armour(fighter)
    apply_weapon(fighter)
    apply_potion(fighter)
