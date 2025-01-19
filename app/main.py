# app/main.py

from battles.battle import Battle
from equipment.armour import Armour
from equipment.potions import Potion
from equipment.weapons import Weapon
from roles.knights import Knight


def battle(knights_config: dict) -> dict:
    def create_knight(data: dict) -> Knight:
        return Knight(
            name=data["name"],
            power=data["power"],
            hp=data["hp"],
            armour=[
                Armour(a["part"], a["protection"]) for a in data["armour"]
            ],
            weapon=Weapon(data["weapon"]["name"], data["weapon"]["power"]),
            potion=Potion(
                data["potion"]["name"],
                data["potion"]["effect"]) if data["potion"] else None,
        )

    lancelot = create_knight(knights_config["lancelot"])
    mordred = create_knight(knights_config["mordred"])
    arthur = create_knight(knights_config["arthur"])
    red_knight = create_knight(knights_config["red_knight"])

    battle1 = Battle(lancelot, mordred).fight()
    battle2 = Battle(arthur, red_knight).fight()

    return {**battle1, **battle2}
