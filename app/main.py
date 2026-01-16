from __future__ import annotations

from app.knight import Knight
from app.items import Weapon, Armour, Potion
import app.config as config


def create_inventory_from(data: dict) -> list[Weapon | Armour | Potion]:
    inventory = [Weapon.from_dict(data["weapon"])]

    if data["potion"] is not None:
        inventory.append(Potion.from_dict(data["potion"]))

    for item in data["armour"]:
        inventory.append(Armour.from_dict(item))

    return inventory


def apply_inventory_on(
        knight: "Knight",
        inventory: list[Weapon | Armour | Potion]
) -> None:
    for item in inventory:
        item.use_on(knight)


def create_roster_from_dict(data: dict) -> dict:
    knights = {}

    for knight_data in data.values():
        knight = Knight.from_dict(knight_data)
        apply_inventory_on(knight, create_inventory_from(knight_data))
        knights.update({knight.name: knight})

    return knights


def battle_between(participant: "Knight", rival: "Knight") -> None:
    print(f"\nBattle between {participant.name} and {rival.name} begins!")

    print(f"{rival.name} strikes first!")
    participant.take_damage(rival.power)

    print(f"{participant.name} fights back!")
    rival.take_damage(participant.power)


def hold_tournament(pairs: tuple, roster: dict) -> None:
    for participant, opponent in pairs:
        battle_between(roster[participant], roster[opponent])


def battle(knights: dict) -> dict:
    pairs = (("Lancelot", "Mordred"), ("Arthur", "Red Knight"))
    roster = create_roster_from_dict(knights)

    hold_tournament(pairs, roster)
    return {knight.name: knight.hp for knight in roster.values()}


print(battle(config.KNIGHTS))
